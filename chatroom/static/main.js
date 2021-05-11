/*
***********************************************************************
SECURITY TOKENS & CONSTANTS
***********************************************************************
*/

const csrftoken = Cookies.get('csrftoken');

/*
***********************************************************************
PRIVATE HELPER FUNCTIONS        
***********************************************************************
*/

function closest(elem, tagname){
    do {
        if (elem.tagName === tagname) return elem;
        elem = elem.parentNode;
    } while (elem);
}

function create_post_request(body) {
    const request = {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', 
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(body)
    };

    return request;
}

function localize_time(utc_time) {
    let date = new Date(utc_time + ' UTC');
    return date;
}

/*
***********************************************************************
CACHED DOM ELEMNTS
***********************************************************************
*/

let userArea_div = document.getElementById("user-area");
let recipientArea_div = document.getElementById("recipient-area");
let messageArea_div = document.getElementById("message-area");
let textSubmitArea_div = document.getElementById("text-submit");
let modalClassmateArea_div = document.getElementById("modal-classmate-area");
let modal_btn = document.getElementById("modal-button");
let searchBar_input = document.getElementById("search-bar");
let activeUserArea_div = document.getElementById("active-user-area");

/*
***********************************************************************
DYNAMIC HTML ELEMENTS
***********************************************************************
*/

let createUserElem = function(user){
    return `<button type="button" class="d-flex list-group-item list-group-item-action justify-content-between align-items-center my-user-button">
                <span class="d-flex align-items-center text-truncate">
                    <i class="fas fa-circle text-primary me-1 ${user.has_notification ? 'visible': 'invisible'}" style="font-size: .5rem;"></i>
                    <i class="fas fa-user-circle fa-lg me-2"></i>
                    <span>${user.other_user}</span>
                </span>
                <span type="span-close-button" class="btn-close my-x-button"></span>
            </button>`;
}
let createToElem = function(to){
    return `<p class="fs-4 p-0 m-0">To: <span id="recipient-area">${to}</span></p>`
}
let createSentMessageElem = function(message){
    return `<div class="chat-bubble sent text-wrap">${message}</div>
            <div class="separator"></div>`;
}
let createReceivedMessageElem = function(message){
    return `<div class="chat-bubble received text-wrap">${message}</div>
            <div class="separator"></div>`;
} 
let createModalClassmateElem = function(classmate){
    return `<button type="button" class="list-group-item list-group-item-action" data-bs-dismiss="modal">${classmate}</button>`;
} 
let createDateTimeElem = function(datetime){
    return `<div class="text-center text-black-50" style="font-size: 0.8rem;">${datetime}</div>`;
} 

/*
***********************************************************************
INIT FUNCTIONS
***********************************************************************
*/

function getActiveUser(){

    /*
     * Right now this is just dummy data but in the future
     * this information should be retrieved from the student model
     */

    let username = activeUserArea_div.children[0].children[0].innerHTML;
    return username;
}

async function getClassmates(activeUser){

    /*
     * Right now this is just dummy data but in the future
     * this information should be retrieved from the backend database
     */
        
    let jsonArray = await fetch_all_users();
    let classmates = jsonArray.map( (jsonObject) => { return jsonObject.username} );

    // remove active user from list
    classmates.splice(classmates.indexOf(activeUser), 1);

    return classmates;
}

async function getUserList(activeUser, classmates){
    const otherUsers = await fetch_user_list(activeUser);
    for(let i = 0; i < otherUsers.length; i++){
        let otherUserName = otherUsers[i].other_user;
        if(classmates.includes(otherUserName)){
            classmates.splice(classmates.indexOf(otherUserName), 1);
        }
    }
    return otherUsers;
}

function getOtherUser(){
    return ( recipientArea_div.children.length != 0 ) ? recipientArea_div.children[0].children[0].innerHTML : '';
}

/*
***********************************************************************
ATTACH/CHAIN DYNAMIC HTML ELEMENTS TO DOM
***********************************************************************
*/

function attachMessageListToMessageDiv(messages, user){
    let postedDate = 0;
    let fiveMinutes = 300000 // milliseconds

    // create HTML list
    let htmlList = messages.reduce( (htmlList, messageObj)=> {
        let newDate = localize_time(messageObj.created_at);
        if (newDate - postedDate > fiveMinutes) {
            htmlList += createDateTimeElem(newDate.toLocaleString('en-US'));            
            postedDate = newDate;
        }

        if(messageObj.from_id === user){
            htmlList += createReceivedMessageElem(messageObj.message);
        } else{
            htmlList += createSentMessageElem(messageObj.message);
        }
        return htmlList;
    }, '');
    // attach html list to modal div
    messageArea_div.innerHTML = htmlList;
    messageArea_div.scrollTop = messageArea_div.scrollHeight;
}

function attachClassmateListToModalDiv(classmates){
    // create HTML list
    let htmlList = classmates.reduce( (htmlList, classmate)=> {
        let elem = createModalClassmateElem(classmate, 0);
        htmlList += elem;
        return htmlList;
    }, '');
    // attach html list to modal div
    modalClassmateArea_div.innerHTML = htmlList;
}

function attachUserListToUserDiv(otherUsers){
    // create HTML list
    let htmlList = otherUsers.reduce( (htmlList, otherUser)=> {
        let elem = createUserElem(otherUser);
        htmlList += elem;
        return htmlList;
    }, '');
    // attach html list to modal div
    userArea_div.innerHTML = htmlList;
}

function attachEmptyElemToMessageDiv(){
    messageArea_div.innerHTML = '';
}

function attachRecipientElemToRecipientDiv(recipient){
    // create HTML recipient element
    let elem = createToElem(recipient);
    recipientArea_div.innerHTML = elem;
}

function chainSentMessageToMessageDiv(message){
    // create HTML recipient element
    let elem = createSentMessageElem(message);
    messageArea_div.innerHTML += elem;
    messageArea_div.scrollTop = messageArea_div.scrollHeight;
}

function chainRecievedMessageToMessageDiv(message){
    // create HTML recipient element
    let elem = createReceivedMessageElem(message);
    messageArea_div.innerHTML += elem;
    messageArea_div.scrollTop = messageArea_div.scrollHeight;
}

/*
***********************************************************************
DATABASE CONNECTION FUNCTIONS
***********************************************************************
*/

async function fetch_conversation(activeUser, otherUser){
    // POST- update db
    const request = create_post_request({
        from: activeUser,
        to: otherUser
    });
    const response = await fetch('retrieve_conversation/', request);
    const messageList = await response.json();

    return messageList;
}

async function fetch_user_list(activeUser){
    // POST- update db
    const request = create_post_request({
        activeUser
    });
    const response = await fetch('retrieve_user_list/', request);
    const jsonArray = await response.json();

    return jsonArray;
}

async function fetch_all_users(){
    // GET- from db
    const response = await fetch('retrieve_all_users/');
    const jsonArray = await response.json();
    return jsonArray;
}

async function fetch_unseen_messages(activeUser, otherUser){
    // POST- retrieve from db
    const request = create_post_request({
        from: otherUser,
        to: activeUser
    });
    // retrieve all unseen messages sent from other user to active user
    const response = await fetch('retrieve_message/', request);
    const jsonArray = await response.json();

    return jsonArray;
}

async function update_messages_as_seen(activeUser, otherUser) {
    // POST- update db
    const request = create_post_request({
        from: activeUser,
        to: otherUser
    });
    const response = await fetch('update_messages_as_seen/', request);
}

async function send_user_list(activeUser, otherUsers){
    // POST- update db
    const request = create_post_request({
        activeUser,
        otherUsers
    });
    const response = await fetch('load_user_list/', request);
}

async function send_message(message, activeUser, otherUser){
    // udpate DOM
    chainSentMessageToMessageDiv(message);

    // POST- update db
    const request = create_post_request({
        message: message,
        from: activeUser,
        to: otherUser
    });
    const response = await fetch('load_message/', request);
}

/*
***********************************************************************
POLLING
***********************************************************************
*/

async function poll_message(activeUser, otherUser){

    /*
     * Only poll for unseen messages if a recipient has been
     * chosen by the active user, otherwise don't send POST
     * request
     */

    if (otherUser !== '') {
        const unseenMessages = await fetch_unseen_messages(activeUser, otherUser);

        // update DOM
        for(let i = 0; i < unseenMessages.length; i++){
            let message = unseenMessages[i]['message'];
            chainRecievedMessageToMessageDiv(message);
        }

        if (unseenMessages.length !== 0) {
            // update unseen messages
            const response = await update_messages_as_seen(activeUser, otherUser);
        }
    } 
}

async function poll_conversation_from_classmatesList(activeUser, classmate, otherUsers, classmates){

    /*
     * poll for entire conversation between user who has
     * not been selected from the classmates list. Once conversation
     * has been polled, see if there are any messages that have not been
     * seen and post the converstaion if so. Otherwise keep polling for new
     * unseen messages
     */

    // POST- retrieve from db
    if(classmates.length !== 0){
        // POST- retrieve from db
        const unseenMessageList = await fetch_unseen_messages(activeUser, classmate);

        if(unseenMessageList.length !== 0){
            // update otherUsers list and remove user from classmates
            let otherUserObj =  { other_user: classmate, has_notification: true };
            otherUsers.unshift(otherUserObj);
            classmates.splice(classmates.indexOf(classmate), 1);
            // update DOM elements
            attachUserListToUserDiv(otherUsers);
        }
    }
}

async function poll_conversation_from_otherUsersList(activeUser, otherUserName, otherUsers){

    // POST- retrieve from db
    if(otherUsers.length !== 0){
        // POST- retrieve from db
        const unseenMessageList = await fetch_unseen_messages(activeUser, otherUserName);

        if(unseenMessageList.length !== 0){
            // update otherUsers list 
            let otherUserObj =  { other_user: otherUserName, has_notification: true };
            // remove user
            let index = otherUsers.findIndex(otherUserObj => { return otherUserObj.other_user === otherUserName; });
            otherUsers.splice(index, 1);
            // update list
            otherUsers.unshift(otherUserObj);
            // update DOM elements
            attachUserListToUserDiv(otherUsers);
        }
    }
}

/*
***********************************************************************
EVENTS        
***********************************************************************
*/

async function modalButtonEvent(e, activeUser, classmates, otherUsers){
    if (e.target === e.currentTarget) return;

    // get index of target button
    let buttons = e.currentTarget.children;
    let index = Array.from(buttons).indexOf(e.target);

    // put classmate into otherUsers and remove classmate from its list
    let otherUserName = classmates[index];
    let otherUserObj =  { other_user: classmates[index], has_notification: false };
    otherUsers.unshift(otherUserObj);
    classmates.splice(index, 1);

    // get cnversation
    const messageList = await fetch_conversation(activeUser, otherUserName);
    // update unseen messages
    const response = await update_messages_as_seen(activeUser, otherUserName);

    // update user area
    attachUserListToUserDiv(otherUsers);
    attachRecipientElemToRecipientDiv(otherUserName);
    attachMessageListToMessageDiv(messageList, otherUserName);

    e.stopPropagation();
}

async function userButtonEvents(e, activeUser, otherUsers, classmates){
    if (e.target === e.currentTarget) return;

    // get span button element from element that was clicked
    let button = closest(e.target, 'BUTTON');                
    let otherUserName = button.children[0].children[2].innerHTML
    let index = otherUsers.findIndex( otherUserObj => { return otherUserObj.other_user === otherUserName; } );

    // close button or user button
    if(e.target.getAttribute('type') === "span-close-button"){
        // update otherUsers and classmates list
        otherUsers.splice(index, 1);
        classmates.push(otherUserName);

        // update DOM
        attachUserListToUserDiv(otherUsers);
        if(otherUsers.length === 0 || index >= otherUsers.length){
            attachEmptyElemToMessageDiv();
            attachRecipientElemToRecipientDiv('');
        } else{
            let nextOtherUserName = otherUsers[index].other_user;
            attachRecipientElemToRecipientDiv(nextOtherUserName);
            attachEmptyElemToMessageDiv();
            const messageList = await fetch_conversation(activeUser, nextOtherUserName);
            attachMessageListToMessageDiv(messageList, nextOtherUserName);
            // update unseen messages
            const response = await update_messages_as_seen(activeUser, nextOtherUserName);
        }
        // must update unseen messages
        const response = await update_messages_as_seen(activeUser, otherUserName);
    } else{
        // update DOM
        const messageList = await fetch_conversation(activeUser, otherUserName);
        attachRecipientElemToRecipientDiv(otherUserName);
        attachMessageListToMessageDiv(messageList, otherUserName);
        // update notification
        otherUsers[index].has_notification = false;
        attachUserListToUserDiv(otherUsers);
        // update unseen messages
        const response = await update_messages_as_seen(activeUser, otherUserName);
    }

    e.stopPropagation();
}

function inputMessageEvent(e, activeUser, otherUser){
    if(e.key === 'Enter'){
        // prevent default page load on keypress
        e.preventDefault();
        // get the current message
        let message = e.target.innerHTML;
        // get the placeholder
        let attr = textSubmitArea_div.getAttributeNode('placeholder');

        /*
         * If a recipient has been selected than send them the message
         * otherwise tell the active user to select a recipient before
         * sending a message
         */

        if (otherUser !== '') {
            send_message(message, activeUser, otherUser);
            attr.textContent = "Message...";
        } else {
            attr.textContent = "You must select a user before sending a message...";
        }

        /*
         * Remove the message from the text area after it has been
         * sent and always keep most recent messages in focus by
         * scrolling to the bottom of the message area div
         */
        
        e.target.innerHTML = '';
        messageArea_div.scrollTop = messageArea_div.scrollHeight;
    }
}

function searchBarEvent(e, otherUsers){
    e.preventDefault();
    let query = e.target.value;

    /*
     * Below we are using Fuse.js- a fuzzy search algorithm in order
     * to properly implement the search functionality. The result of 
     * the search algorithm is an array of values that match the give 
     * search value in order of closest match
     */

    const fuse = new Fuse(otherUsers, {keys: ['other_user']});
    const result = fuse.search(query);
    const filter = result.map( (o) => { return o.item; } );

    if(query !== ''){
        // show filtered search
        attachUserListToUserDiv(filter);
    } else{
        // show full user list
        attachUserListToUserDiv(otherUsers);
    }
}

async function unloadEvent(e, activeUser, otherUsers){
    send_user_list(activeUser, otherUsers);
}

// attach event handlers
async function main(){
    // get active user, classmates, and a list of other users
    let activeUser = getActiveUser();
    let classmates = await getClassmates(activeUser);
    let otherUsers = await getUserList(activeUser, classmates);

    // default DOM updates
    attachUserListToUserDiv(otherUsers);

    // add-new-user button event
    modal_btn.addEventListener('click', (e) => { attachClassmateListToModalDiv(classmates); }, false);
    // modal button event
    modalClassmateArea_div.addEventListener('click', (e) => { await modalButtonEvent(e, activeUser, classmates, otherUsers); }, false);
    // user button event
    userArea_div.addEventListener('click', (e) => { await userButtonEvents(e, activeUser, otherUsers, classmates); }, false);
    // message input area event
    textSubmitArea_div.addEventListener('keypress', (e) => { inputMessageEvent(e, activeUser, getOtherUser()); }, false);
    // search bar event
    searchBar_input.addEventListener('input', (e)=>{ searchBarEvent(e, otherUsers); }, false);
    // close window event
    window.addEventListener('beforeunload', (e)=>{ await unloadEvent(e, activeUser, otherUsers); }, false);

    /*
     * The below pollings represent retrievals of new, unseen messages. Therefore, a blue
     * dot to the left of the user name and profile icon should be displayed upon every
     * new message.
     */

    // poll for new unseen messages
    setInterval(async () => {
        await poll_message(activeUser, getOtherUser());
    }, 100);

    // poll for new conversations from classmate list
    setInterval(() => {
        classmates.forEach( async (classmate) => {
            await poll_conversation_from_classmatesList(activeUser, classmate, otherUsers, classmates);
        }); 
    }, 400);

    // poll for new conversations from otherUsers list
    setInterval(() => {
        otherUsers.forEach( async (otherUserObj) => {
            if (otherUserObj.has_notification === false && otherUserObj.other_user !== getOtherUser()) {
                await poll_conversation_from_otherUsersList(activeUser, otherUserObj.other_user, otherUsers);
            }
        }); 
    }, 400);
}

// APP
// 1.) For next feature, do timestamp!

// UI:
// 1.) Make sidebar card a bluish color with white text
// 2.) Make search bar translucent

// run app
main();