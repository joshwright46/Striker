$(document).ready(function () {
    $("#info").click(function () {
        $("#info_panel").slideDown();
        $("#recent_panel").slideUp();
        $("#favorites_panel").slideUp();
    });

    $("#recent").click(function () {
        $("#recent_panel").slideDown();
        $("#info_panel").slideUp();
        $("#favorites_panel").slideUp();
    });

    $("#favorites").click(function () {
        $("#favorites_panel").slideDown();
        $("#info_panel").slideUp();
        $("#recent_panel").slideUp();
    });
});