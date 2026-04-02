# Convert Spectrogram

Projeto Python para **converter arquivos de áudio `.wav` em imagens de mel-spectrogram**. As imagens geradas são salvas organizadas por categoria, prontas para uso em pipelines de machine learning.

---

## Como funciona

O projeto percorre uma pasta de áudios organizada por subpastas (categorias), converte cada arquivo `.wav` em um mel-spectrogram e salva o resultado como imagem `.jpg` na pasta `dataset/`.

```
audios/
├── gato/
│   ├── audio1.wav  →  dataset/gato/audio1.jpg
│   └── audio2.wav  →  dataset/gato/audio2.jpg
└── cachorro/
    └── audio3.wav  →  dataset/cachorro/audio3.jpg
```

Internamente, o áudio passa pelo seguinte processo:

1. Carregamento do `.wav` com `librosa`
2. Geração do **mel-spectrogram**
3. Conversão para escala de decibéis (`power_to_db`)
4. Salvamento como imagem `.jpg` (0.72×0.72 pol, 400 DPI)

---

## Tecnologias utilizadas

| Biblioteca | Descrição |
|---|---|
| [librosa](https://librosa.org/) | Carregamento de áudio e geração do mel-spectrogram |
| [numpy](https://numpy.org/) | Operações numéricas |
| [matplotlib](https://matplotlib.org/) | Renderização e salvamento das imagens |
| [uv](https://docs.astral.sh/uv/) | Gerenciamento de dependências |

**Python:** 3.13+

---

## Instalação

### Pré-requisitos

- Python 3.13 ou superior
- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado

### Passos

```bash
# Clone o repositório
git clone https://github.com/arielfernandes/convert_spectrogram.git
cd convert_spectrogram

# Instale as dependências
uv sync

# Execute o projeto
uv run main.py
```

---

## Como usar

Organize seus arquivos de áudio em subpastas dentro de uma pasta chamada `audios/`, onde cada subpasta representa uma categoria:

```
audios/
├── categoria_a/
│   ├── audio1.wav
│   └── audio2.wav
└── categoria_b/
    └── audio3.wav
```

Em seguida, execute o script:

```bash
uv run main.py
```

As imagens serão geradas automaticamente na pasta `dataset/`, mantendo a mesma estrutura de categorias.

> ⚠️ Se a pasta `dataset/<categoria>` já existir, ela será **apagada e recriada** a cada execução.

---

## Estrutura do projeto

```
convert_spectrogram/
├── audio_image/       # Pacote principal com a lógica de conversão
├── main.py            # Ponto de entrada do projeto
├── pyproject.toml     # Configuração do projeto e dependências
├── poetry.lock        # Versões travadas das dependências
└── README.md
```
