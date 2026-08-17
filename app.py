import qrcode
import os

def gerar_qr_code(url_destino, nome_arquivo="qrcode_projeto.png"):
    # Garante que a pasta assets existe
    pasta_destino = "assets"
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)

    # Configuração do QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Adiciona a URL do seu GitHub ou LinkedIn
    qr.add_data(url_destino)
    qr.make(fit=True)

    # Gera e salva a imagem
    img = qr.make_image(fill_color="#1a1a1a", back_color="white")
    img.save(caminho_completo)
    
    print(f"✅ Sucesso! QR Code gerado em: {caminho_completo}")
    print(f"Ele aponta para: {url_destino}")

if __name__ == "__main__":
    # TODO:
    meu_github_url = "https://github.com/dlorodrigues/stellantis_inovacao_ia"
    gerar_qr_code(meu_github_url)
