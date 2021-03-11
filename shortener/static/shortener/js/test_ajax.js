function ajaxPagination() {
    $('#paginationId a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')
            console.log(page_url)
            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $("#pagination-link").empty()
                    $("#pagination-link").append($(data).find("#pagination-link").html())

                    $("#paginationId").empty()
                    $("#paginationId").append($(data).find("#paginationId").html())
                }
            })
        })
    })
}

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

    $("#button-replace").click(function(){
        var serializedData = $("#shortForm").serialize();
        $.ajax({
            url: $("#shortForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $("#shortForm").html('<div class="row g-2"><div class="col-md-8"><input class="form-control form-control-lg" type="text" value="' + response.short_link + '" aria-label=".form-control-lg example" readonly></div><div class="col-md"><button type="button" class="btn btn-primary btn-lg mx-4" id="button-replace" style="width: 100%">Copied</button></div></div>')
            }
        })
        console.log('Done')

    });

    ajaxPagination()
});

$(document).ajaxStop(function() {
    ajaxPagination()
})
