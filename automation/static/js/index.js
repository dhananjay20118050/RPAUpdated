let table = $('#datatables').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": {
        "url": "/api/nodes/",
        "type": "GET"
    },
    "columns": [
        {"data": "id"},
        {"data": "name"},
        {"data": "ip"},
        {"data": "port"},
        { defaultContent: '<div class="badge badge-danger">Not Active</div>'},
        {
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-info btn-primary" href="/edit/{{id}}"><i class="far fa-edit"></i></button>' + '&nbsp;&nbsp' +
            '<button type="button" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>'
        }
    ]


});

let id = 0;

$('#datatables tbody').on('click', 'button', function () {
    let data = table.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info btn-primary') {
        // EDIT button
        window.location.href = '../edit/'+data['id'];
        /*$('#name').val(data['name']);
        $('#password').val(data['password']);
        $('#email').val(data['email']);
        $('#roleid').val(data['roleid']);*/

        //$('#type').val('edit');
       // $('#modal_title').text('EDIT');
        //$("#myModal").modal();
    } else {
        // DELETE button

        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['id'];


});

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    let url = '/api/hubs/';

    if (type == 'new') {
        // new
        method = 'POST';
    } else {
        // edit
        id = $('#dataid').val();
        url = url + id + '/';
        method = 'PUT';
    }
    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        //console.log(data);
        //location.reload();
      //window.location.href = '/Nodes/';
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

//$('#confirm').on('click', '#delete', function (e) {
$('#delete').click(function(e){
var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: '/api/nodes/' + id + '/',
        headers:{"X-CSRFToken": $crf_token},
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


/*$('#new').on('click', function (e) {
    $('#name').val('');
    $('#email').val('');
    $('#roleid').val('');
    $('#type').val('new');
    $('#modal_title').text('NEW USER');
    $("#myModal").modal();
});*/


