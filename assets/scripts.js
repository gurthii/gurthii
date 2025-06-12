/*
Chunya, app that:
- takes product details, 
- validates them, and 
- displays them.
*/

document.getElementById("productForm").addEventListener("submit", function(event) { 
    event.preventDefault(); //with event listener instead of an onsubmit attribute
    let input = document.getElementById("productDetails").value;
    document.getElementById("result").textContent = `You entered: ${input}`;
});

// document.querySelector("span.-b.-ubpt.-tal.-fs24.-prxs").textContent
// above line could work but scraping with JavaScript is not recommended due to CORS issues and other limitations. Instead, use server-side scraping or APIs if available. Or handle it with a backend service that fetches the data and sends it to the frontend.

/*
Hover.io, app that:
- tracks lifetime and unique hover points on a page
- displays a heatmap if prompted by user, else just a blank page with a button/question
*/