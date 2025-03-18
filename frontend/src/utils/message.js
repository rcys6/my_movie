import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"


export default function showMessage(message,status='error',Callback_func){

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
        duration: 2000,
        destination: "https://github.com/apvarun/toastify-js",
        newWindow: true,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: background_color,
        },

        callback:function () {
            if (!Callback_func) return
            if (Callback_func)
            {
                Callback_func()
            }
        },

 
        onClick: function(){} // Callback after click
        }).showToast();
}