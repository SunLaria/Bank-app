
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
