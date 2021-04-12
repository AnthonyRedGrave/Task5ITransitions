function toggle(source) {

    const checkboxes =  document.getElementsByClassName('checkall')
    for (var i = 0; i< checkboxes.length; i++){
        checkboxes[i].checked = source.checked
    }
}


