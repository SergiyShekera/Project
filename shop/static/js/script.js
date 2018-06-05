var HttpClient = function () {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function () {
            if(anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        };
        anHttpRequest.open("Get", aUrl, true);
        anHttpRequest.send(null);
    };
};

var the_url_prod_list = 'http://localhost:8080/shop/api/prod-list';
// var the_url = 'http://localhost:8080/shop/api/prod-category-list-by/1/';
var client = new HttpClient();
    client.get(the_url_prod_list, function  (response) {
        var response1 = JSON.parse(response);
        // alert(response);
        var prod = [];
        for (var key in response1) {

            prod.push("<a href = 'http://localhost:8080/shop/api/prod-detail/" + response1[key].id + "'" + "<p>"
                + " <img src=" + response1[key].image + " class='cart-img'> "  + "name: " + response1[key].name
                + " " + "price: " + response1[key].price + "</br>" + "</p>" + "</a>" );

            };

document.getElementById("prod_list").innerHTML = prod.join('');

    });



var the_url_cat_list = 'http://localhost:8080/shop/api/prod-category-list';
var client = new HttpClient();
    client.get(the_url_cat_list, function(response) {
        var response1 = JSON.parse(response);
        // alert(response);
        var cat =[];
        for (var key in response1) {

            cat.push("<a href = 'http://localhost:8080/shop/api/prod-detail/" + response1[key].id + "'" +
                "<p>" + response1[key].name  + "</p>" + "</a>");
            };

document.getElementById("cat_list").innerHTML = cat.join('');

    });

