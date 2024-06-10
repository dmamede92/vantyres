$( document ).ready(function() {
    $('.phone').mask('(00) 00000-0000');
    $('.cep').mask('00000-000');
    $('.data_nascimento').mask('00/00/0000');
    $('.rg').mask('00.000.000-0');

    var baseUrl = 'http://localhost:8000/';
    var deleteBtn = $('.delete-btn');
    var tipo = $('.id_tipo');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var cepForm = $('#cep-form');
    var filter = $('#filter');
    var tipoPessoaSelect = $('#id_tipo');
    var cpfCnpjInput = $('.cpf_cnpj');

    function aplicarMascaraCpfCnpj(tipoPessoa) {
        if (tipoPessoa === 'fis') {
            cpfCnpjInput.mask('000.000.000-00', { reverse: true });

        } else if (tipoPessoa === 'jud') {
            cpfCnpjInput.mask('00.000.000/0000-00', { reverse: true });

        } else {
            cpfCnpjInput.unmask();
        }
    }

    aplicarMascaraCpfCnpj(tipoPessoaSelect.val());

    tipoPessoaSelect.change(function() {
        aplicarMascaraCpfCnpj($(this).val());
    });

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja remover?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(cepForm).on('click', function() {
        cepForm.submit();
    });


    $(filter).change(function() {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });

    document.getElementById("btn-consultar-cep").addEventListener("click", function() {
        var cep = document.getElementById("id_cep").value;

        fetch("https://viacep.com.br/ws/" + cep + "/json/")
            .then(response => response.json())
            .then(data => {
                document.getElementById("id_logradouro").value = data.logradouro;
                document.getElementById("id_cidade").value = data.localidade;
                document.getElementById("id_estado").value = data.uf;
            })
            .catch(error => console.error('Erro ao consultar o CEP:', error));
    });
});

function remove_mask(form){
    $(".phone").unmask();
    $('.cep').unmask();
    $('.cpf_cnpj').unmask();
    $('.rg').unmask();
}

function toggleDivs() {
        var hideDiv = document.getElementById('client-info');
        var hideDiv2 = document.getElementById('contact-info');
        var hideDiv3 = document.getElementById('address-info');
        var hideDiv4 = document.getElementById('control_submit');
        var hideDiv5 = document.getElementById('add_vehicle_form');
        var hideDiv6 = document.getElementById('table_vehicle');
        var showDiv = document.getElementById('vehicle_form');
        var showDiv2 = document.getElementById('control_vehicle');

        hideDiv.style.display = "none";
        hideDiv2.style.display = "none";
        hideDiv3.style.display = "none";
        hideDiv4.style.display = "none";
        hideDiv5.style.display = "none";
        hideDiv6.style.display = "none";

        showDiv.style.display = "block";
        showDiv2.style.display = "block";

}

function toggleShow2() {
        var hideDiv = document.getElementById('client-info');
        var hideDiv2 = document.getElementById('contact-info');
        var hideDiv3 = document.getElementById('address-info');
        var hideDiv4 = document.getElementById('control_submit');
        var hideDiv5 = document.getElementById('add_vehicle_form');
        var hideDiv6 = document.getElementById('table_vehicle');
        var showDiv = document.getElementById('vehicle_form');
        var showDiv2 = document.getElementById('control_vehicle');

        hideDiv.style.display = "block";
        hideDiv2.style.display = "block";
        hideDiv3.style.display = "block";
        hideDiv4.style.display = "block";
        hideDiv5.style.display = "block";
        hideDiv6.style.display = "block";

        showDiv.style.display = "none";
        showDiv2.style.display = "none";

}

function toggleDivs2(hideDivId, showDivId, tableDiv) {
        var hideDiv = document.getElementById(hideDivId);
        var showDiv = document.getElementById(showDivId);
        var hideTableDiv = document.getElementById(tableDiv);

        hideDiv.style.display = "none";
        hideTableDiv.style.display = "none";
        showDiv.style.display = "block";
}

function toggleShow(hideDivId, showDivId, tableDiv) {
    var hideDiv = document.getElementById(hideDivId);
    var showDiv = document.getElementById(showDivId);
    var hideTableDiv = document.getElementById(tableDiv);

    hideDiv.style.display = "block";
    hideTableDiv.style.display = "block";
    showDiv.style.display = "none";
}