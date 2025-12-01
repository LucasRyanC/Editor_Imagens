from PIL import Image, ImageFilter
import os

# --- 1. FUNÇÕES DE MANIPULAÇÃO ---

def converter_para_cinza(caminho_entrada, caminho_saida):
    """Converte a imagem para escala de cinza e salva."""
    try:
        img = Image.open(caminho_entrada)
        # O método .convert('L') faz a conversão para Grayscale
        img_cinza = img.convert('L')
        img_cinza.save(caminho_saida)
        print(f"✅ Imagem convertida para Grayscale salva em: {caminho_saida}")
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado no caminho: {caminho_entrada}")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

def redimensionar_e_salvar(caminho_entrada, caminho_saida, largura, altura):
    """Redimensiona a imagem para o tamanho desejado."""
    try:
        img = Image.open(caminho_entrada)
        # O método .resize() altera o tamanho
        img_redimensionada = img.resize((largura, altura))
        img_redimensionada.save(caminho_saida)
        print(f"✅ Imagem redimensionada para {largura}x{altura} salva em: {caminho_saida}")
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado no caminho: {caminho_entrada}")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# --- 2. MENU PRINCIPAL (Interface CLI) ---

def menu_principal():
    print("\n--- EDITOR DE IMAGENS PYTHON (PILLOW) ---")
    caminho_original = input("▶️ Digite o NOME do arquivo de imagem (ex: foto.jpg): ")
    
    if not os.path.exists(caminho_original):
        print("❌ Arquivo não encontrado. Verifique o nome e tente novamente.")
        return

    while True:
        print("\nEscolha a transformação:")
        print("1. Converter para Tons de Cinza")
        print("2. Redimensionar")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            nome, ext = os.path.splitext(caminho_original)
            caminho_saida = f"{nome}_grayscale{ext}"
            converter_para_cinza(caminho_original, caminho_saida)
        
        elif opcao == '2':
            try:
                largura = int(input("Nova Largura (px): "))
                altura = int(input("Nova Altura (px): "))
                nome, ext = os.path.splitext(caminho_original)
                caminho_saida = f"{nome}_resized_{largura}x{altura}{ext}"
                redimensionar_e_salvar(caminho_original, caminho_saida, largura, altura)
            except ValueError:
                print("⚠️ Largura e Altura devem ser números inteiros.")

        elif opcao == '3':
            print("Encerrando o Editor. Valeu!")
            break
        
        else:
            print("Opção inválida. Tente 1, 2 ou 3.")

# Inicia o programa
if __name__ == "__main__":
    menu_principal()