

const url = "https://script.google.com/macros/s/AKfycbwwMBib3Wbg2elAAIWstZx4UBygHw6kX3RXUmo7jEjs1Xw12xEJOSUMYe_L02quGIze/exec"
    const form = document.forms['dform']
            await form.addEventListener('submit', e => {
        e.preventDefault();
    fetch(url, {method: 'POST', body: new FormData(form) })
                    .then(response => alert("thank you"))

                    .catch(error => console.error("error"))
            });
