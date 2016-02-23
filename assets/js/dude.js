
function queryString(){
    var msg = window.location.search.substring(1);
    if (msg){
        alert("  \t\tHey, " + msg+'!\n\
    You MUST pass model instance to the templatetag!\n\
    Have a nice weekend! %-)')
    };
};

window.onload=function(){
    queryString();
};