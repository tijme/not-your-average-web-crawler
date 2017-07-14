var releases = {"1.4.7": true, "1.5.0": true, "1.5.1": true, "1.5.2": true, "1.6.3": true, "1.6.4": true, "1.6.5": true, "1.7.0": true}


$(document).ready(function() {
    var latestVersion = Object.keys(releases)[Object.keys(releases).length - 1];
    var currentVersion = $('#releases').attr('data-selected');

    /**
     * Generate dropdown
     */
    var dropdownHtml = "";

    Object.keys(releases).forEach(function(version, index) {
        var isLatest = version == latestVersion
        var labelHtml = isLatest ? " <span class=\"badge\">latest</span>" : "";
        var labelLink = '../' + (isLatest ? 'latest' : version) + '/index.html';

        dropdownHtml = "<li><a href=\"" + labelLink + "\">Version " + version + labelHtml + "</a></li>" + dropdownHtml;
    });

    $('#releases .dropdown-menu').html(dropdownHtml);

    /**
     * Show message if not viewing the latest version
     */
    if (latestVersion != currentVersion) {
        var message = "<strong>Warning!</strong> Version <a href=\"../latest/index.html\">" + latestVersion + "</a> is available (you are currently viewing version " + currentVersion + ").";
        var messageHtml = '<div class="container"><div class="row"><div class="col-lg-10 col-lg-offset-1"><div class="alert alert-danger" role="alert">' + message + '</div></div></div></div>';
        $(messageHtml).insertAfter($('.jumbotron'))
    }
});
