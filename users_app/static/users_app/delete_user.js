//function delete_user(){
//    e.preventDefault()
//    console.log('удалить')
//    const checkboxes =  document.getElementsByClassName('checkall')
//    const delete_url = 'https://127.0.0.1:8000/users/delete/'
//    const csrf = document.getElementsByName('csrfmiddlewaretoken')
//    console.log(csrf[0].value)
//    for (var i = 0; i< checkboxes.length; i++){
//        console.log(checkboxes[i].value)
//
//
//    }
//
//})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const delete_button = $(".delete_button")[0]
const csrftoken = getCookie('csrftoken');
delete_button.addEventListener('click', function(e){
    e.preventDefault()
    const checkboxes =  document.getElementsByClassName('checkall')
    for (var i = 0; i< checkboxes.length; i++){
        if(checkboxes[i].checked == true){
            var url = `https://127.0.0.1:8000/users/delete/${checkboxes[i].value}/`
//            fetch(url, {
//                method: 'DELETE',
//                headers:{
//                    'Content-type': 'applications/json',
//                    'X-CSRFToken': csrftoken,
//                }
//            }).then(function(response){
//                console.log(response)
//                })
            $.ajax({
                type: 'DELETE',
                url: url,
                dataType: "json",
                success: function (response) {
                    console.log(response)

                },
                error: function (response) {
                    console.log(response)

                }
    })

        }



    }
})
