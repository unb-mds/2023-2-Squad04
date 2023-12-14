# Branch de Testes

Esta branch é dedicada exclusivamente para testes no projeto.

## Atenção!
Antes de rodar o teste, altere a data no arquivo src/pdf_downloader_last_date.txt para uma data posterior não muito distante da atual. Isso é importante porque os PDFs serão baixados durante o teste.

Certifique-se de ter o Pytest instalado. Se ainda não estiver instalado, use o seguinte comando:
```
pip install pytest
```

**Ao executar o teste, por favor, siga estas instruções:**

1. Certifique-se de estar na raiz do projeto
2. Execute:

```
python3 -m pytest
```