const form = document.getElementById('subscriptionForm');
form.addEventListener('submit', async event => {
    event.preventDefault();
    var resultsDiv = document.getElementById('formResults');
    resultsDiv.innerHTML="<p>Loading...</p>"
    var emailInput = document.getElementById('emailInput').value;
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            email: emailInput
        })
    };
    const response = await fetch('https://2qvg3umde5.execute-api.us-east-1.amazonaws.com/prod/subscribe', requestOptions);
    const status = await response.status;
    if (status === 200) {
        resultsDiv.innerHTML="<br /><div class=\"alert alert-success\" role=\"alert\">You have successfully registered to receive email notifications.</div>";
    } else {
        resultsDiv.innerHTML="<br /><div class=\"alert alert-danger\" role=\"alert\">Your response could not be submitted.  Error code " + status + "</div>";
    }
})