{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rosnittaa/ml-day-1/blob/main/textsummarization.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "from nltk.corpus import stopwords\n",
        "from nltk.tokenize import word_tokenize, sent_tokenize\n",
        "from heapq import nlargest\n",
        "\n",
        "# Download nltk resources if not already downloaded\n",
        "nltk.download('punkt')\n",
        "nltk.download('stopwords')\n",
        "\n",
        "def text_summarizer(text, num_sentences=3):\n",
        "    # Tokenize the text into sentences\n",
        "    sentences = sent_tokenize(text)\n",
        "\n",
        "    # Tokenize the text into words\n",
        "    words = word_tokenize(text)\n",
        "\n",
        "    # Remove stopwords\n",
        "    stop_words = set(stopwords.words('english'))\n",
        "    words = [word for word in words if word.lower() not in stop_words]\n",
        "\n",
        "    # Calculate word frequencies\n",
        "    word_freq = {}\n",
        "    for word in words:\n",
        "        if word in word_freq:\n",
        "            word_freq[word] += 1\n",
        "        else:\n",
        "            word_freq[word] = 1\n",
        "\n",
        "    # Calculate sentence scores based on word frequencies\n",
        "    sentence_scores = {}\n",
        "    for sentence in sentences:\n",
        "        for word in word_tokenize(sentence.lower()):\n",
        "            if word in word_freq:\n",
        "                if sentence not in sentence_scores:\n",
        "                    sentence_scores[sentence] = word_freq[word]\n",
        "                else:\n",
        "                    sentence_scores[sentence] += word_freq[word]\n",
        "\n",
        "    # Select the top 'num_sentences' sentences with highest scores\n",
        "    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)\n",
        "    summary = ' '.join(summary_sentences)\n",
        "\n",
        "    return summary\n",
        "\n",
        "# Main function\n",
        "def main():\n",
        "    # Input text from the user\n",
        "    text = input(\"Enter the text you want to summarize:\\n\")\n",
        "\n",
        "    # Set the number of sentences in the summary\n",
        "    num_sentences = int(input(\"Enter the number of sentences for the summary (default is 3): \") or 3)\n",
        "\n",
        "    # Generate summary\n",
        "    summary = text_summarizer(text, num_sentences)\n",
        "    print(\"\\nSummary:\")\n",
        "    print(summary)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PjKfr1SUnxcC",
        "outputId": "3d68095d-507d-4029-c765-fcee2a59a555"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers/punkt.zip.\n",
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the text you want to summarize:\n",
            "The advancement of artificial intelligence has revolutionized various industries, including healthcare, finance, and transportation. AI-powered technologies such as machine learning and natural language processing have enabled businesses to automate tasks, analyze data more efficiently, and improve decision-making processes. However, concerns have been raised regarding the ethical implications of AI, particularly regarding privacy, bias, and job displacement. Despite these challenges, the potential benefits of AI continue to drive research and development efforts worldwide.\n",
            "Enter the number of sentences for the summary (default is 3): 5\n",
            "\n",
            "Summary:\n",
            "However, concerns have been raised regarding the ethical implications of AI, particularly regarding privacy, bias, and job displacement. The advancement of artificial intelligence has revolutionized various industries, including healthcare, finance, and transportation. AI-powered technologies such as machine learning and natural language processing have enabled businesses to automate tasks, analyze data more efficiently, and improve decision-making processes. Despite these challenges, the potential benefits of AI continue to drive research and development efforts worldwide.\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}