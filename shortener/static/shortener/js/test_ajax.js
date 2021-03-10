$(document).ready(function(){
    $("#button-addon2").click(function(){
        var serializedData = $("#shortLinkForm").serialize();
        $.ajax({
            url: $("#shortLinkForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $("#shortLink").append('<form method="post"><div class="input-group mb-3 my-3"><input type="text" class="form-control" value="' + response.short_link + '" aria-label="short-url" aria-describedby="button-addon3" readOnly><button class="btn btn-outline-primary" type="submit" id="button-addon3">Copied!</button></div></form>')
            }
        })
        console.log('Done')

    });
});

