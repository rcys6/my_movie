import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"


export default function showMessage(message,status='error'){

    let background_color;
    if(status == 'error' )
    {
        background_color="linear-gradient(to right, #ff5f6d, #ffc371)"
    }
    else if(status == 'nomal')
    {
        background_color="linear-gradient(to right, #00b09b, #96c93d)"
    }

    Toastify({
        text: message,
        duration: 3000,
        destination: "https://github.com/apvarun/toastify-js",
        newWindow: true,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: background_color,
        },
        onClick: function(){} // Callback after click
        }).showToast();
}