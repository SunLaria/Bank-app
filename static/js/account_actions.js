
function getCSRFToken() {
    const cookieString = document.cookie;
    const cookies = cookieString.split(';');
    let csrfToken = null;

    cookies.forEach(cookie => {
        const cookieParts = cookie.trim().split('=');
        const cookieName = cookieParts[0];
        const cookieValue = cookieParts[1];

        if (cookieName === 'csrftoken') {
            csrfToken = cookieValue;
        }
    });

    return csrfToken;
}


function deposit(params) {
    axios.post('/api/deposit/', {amount: params.amount, description: params.description},{headers: {
        'X-CSRFTOKEN': getCSRFToken()}})
    .then((response)=>{console.log(response.data);})
}

// deposit({amount:16,description:"dsada"})

function withdraw(params) {
    axios.post('/api/withdraw/', {amount: params.amount, description: params.description},{headers: {'X-CSRFTOKEN': getCSRFToken()}})
    .then((response)=>{console.log(response.data);})
}

// withdraw({"amount": 500, "description": "withdraw description"})

function transfer(params) {
    axios.post('/api/transfer/', {amount: params.amount, to_account_number:params.to_account_number, description: params.description},{headers: {
        'X-CSRFTOKEN': getCSRFToken()
    }})
    .then((response)=>{console.log(response.data);})
}

// {"amount": 12121, "to_account_number": 123123, "description": "transfer description"}