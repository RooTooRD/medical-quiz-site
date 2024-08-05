const url = window.location.href;

const questionBox = document.getElementsByClassName('feed')[0]; // Select the first element



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrftoken');




$(document).ready(function () {

    $.ajax({

        type: 'GET',
        url: `${url}data`,
        success: function (response) {
            // Loop through each item in the data array
            response.data.forEach(item => {
                // Each item is an object, so we can access the key and value
                for (const question in item) {
                    const choices = item[question]; // The array of answers

                    // Create a question card for each question
                    let [question_text, question_id] = question.split(';;;;;')
                    // let questionCardHTML = `
                    //     <div class="card mb-3 question-card">
                    //         <div class="card-body">
                    //             <form action="${url}answer/" method="POST" class="answer-form">
                    //                 <input type="hidden" name="id" value="${question_id}" >
                    //                 <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                    //                 <h5 class="card-title">${question_text}</h5>
                    // `;
                    let questionCardHTML = `
                    <div class="mb-4 p-4 bg-white shadow-md rounded-lg question-card">
                        <div class="card-body">
                            <form action="${url}answer/" method="POST" class="answer-form">
                                <input type="hidden" name="id" value="${question_id}">
                                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                <h5 class="text-lg font-semibold mb-3">${question_text}</h5>
                    `
                  
                    // Loop through each choice and create a checkbox
                    choices.forEach(choice => {
                        let [choice_text, choice_id] = choice.split(';;;;;')
                    
                        // questionCardHTML += `
                        //     <div class="form-check p-2  mb-2 bg-secondary bg-gradient bg-opacity-10">
                        //         <input class="form-check-input big-checkbox" type="checkbox" id="${question_id}-${choice_id}" name="${choice_id}" value="${choice_text}">
                        //         <label class="form-check-label " for="${question_text}-${choice_text}">${choice_text}</label>
                        //     </div>
                        // `;
                        questionCardHTML += `
                            <div class="form-check p-2 mb-2 bg-gray-200 rounded">
                                <input class="form-check-input big-checkbox" type="checkbox" id="${question_id}-${choice_id}" name="${choice_id}" value="${choice_text}">
                                <label class="form-check-label" for="${question_text}-${choice_text}">${choice_text}</label>
                            </div>
                        `
                        
                    });

                    // questionCardHTML += `
                    //                 <button type="submit-answer" class="btn btn-primary mt-2">Submit Answer</button>
                    //             </form>
                    //         </div>
                    //     </div>
                    // `;
                    questionCardHTML += `
                        <button type="submit-answer" class="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Submit Answer</button>
                                </form>
                            </div>
                        </div>
                    
                    `

                    questionBox.innerHTML += questionCardHTML; // Append the constructed HTML to questionBox
                }
            });
            const formsList = document.getElementsByClassName('answer-form')
            const formsArray = Array.from(formsList)
            formsArray.forEach( form => {
            
                form.addEventListener('submit', function(event) {
                    event.preventDefault();
                    const formData = $(this).serialize()
                    // console.log(formData)
                    $.ajax({
                        type: 'POST',
                        url: `${url}answer/`,
                        data: formData,
                        success: function(response){
                            let question = response.question

                            let checked_true = response.checked_true
                            let checked_false = response.checked_false
                            let unchecked_true = response.unchecked_true
                            

                            checked_true.forEach(id => {
                                
                                let div = $('div.form-check').has(`input#${question}-${id}`);
                                // div.css('background-color', 'green');
                                // div.addClass('bg-success bg-opacity-25');
                                div.addClass('bg-green-500 bg-opacity-25');

                            })

                            checked_false.forEach(id => {
                                let div = $('div.form-check').has(`input#${question}-${id}`);
                                // div.addClass('bg-danger bg-opacity-25');
                                div.addClass('bg-red-500 bg-opacity-25');
                            })

                            unchecked_true.forEach(id => {
                                let div = $('div.form-check').has(`input#${question}-${id}`);
                                // div.addClass('bg-danger bg-opacity-25');
                                div.addClass('bg-red-500 bg-opacity-25');

                                
                            })


                            



                        },
                        error: function(error){

                        }
                    })
                })
            })
        },
        error: function (error) {
            console.log(error);
        }
    });

    

});



