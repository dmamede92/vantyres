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
