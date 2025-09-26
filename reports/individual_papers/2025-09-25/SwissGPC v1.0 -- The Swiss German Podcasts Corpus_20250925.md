---
keywords:
  - Swiss German Speech Corpus
  - Dialect Identification
  - Spontaneous Speech
  - Automated Annotation
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19866
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:46:21.361580",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Swiss German Speech Corpus",
    "Dialect Identification",
    "Spontaneous Speech",
    "Automated Annotation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Swiss German Speech Corpus": 0.78,
    "Dialect Identification": 0.7,
    "Spontaneous Speech": 0.77,
    "Automated Annotation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Swiss German speech",
        "canonical": "Swiss German Speech Corpus",
        "aliases": [
          "Swiss German Audio",
          "Swiss German Dataset"
        ],
        "category": "unique_technical",
        "rationale": "This corpus is a unique resource for studying spontaneous Swiss German speech, which is crucial for dialect research and ASR development.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "dialect identification",
        "canonical": "Dialect Identification",
        "aliases": [
          "Dialect Recognition",
          "Dialect Detection"
        ],
        "category": "specific_connectable",
        "rationale": "Dialect identification is a specific task that benefits from the corpus, linking it to broader language processing research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "spontaneous conversations",
        "canonical": "Spontaneous Speech",
        "aliases": [
          "Natural Conversations",
          "Unscripted Speech"
        ],
        "category": "unique_technical",
        "rationale": "Capturing spontaneous speech is essential for real-world applications, differentiating this corpus from others.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "automated annotation pipeline",
        "canonical": "Automated Annotation",
        "aliases": [
          "Annotation Pipeline",
          "Automatic Labeling"
        ],
        "category": "specific_connectable",
        "rationale": "Automated annotation is a key process in corpus creation, relevant to machine learning and data processing.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.76,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "corpus construction methodology",
      "token counts",
      "segmentation characteristics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Swiss German speech",
      "resolved_canonical": "Swiss German Speech Corpus",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "dialect identification",
      "resolved_canonical": "Dialect Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "spontaneous conversations",
      "resolved_canonical": "Spontaneous Speech",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "automated annotation pipeline",
      "resolved_canonical": "Automated Annotation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.76,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# SwissGPC v1.0 -- The Swiss German Podcasts Corpus

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19866.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19866](https://arxiv.org/abs/2509.19866)

## 🔗 유사한 논문
- [[2025-09-23/WenetSpeech-Chuan_ A Large-Scale Sichuanese Corpus with Rich Annotation for Dialectal Speech Processing_20250923|WenetSpeech-Chuan: A Large-Scale Sichuanese Corpus with Rich Annotation for Dialectal Speech Processing]] (80.7% similar)
- [[2025-09-24/SloPalSpeech_ A 2,8000-Hour Slovak Speech Corpus from Parliamentary Data_20250924|SloPalSpeech: A 2,8000-Hour Slovak Speech Corpus from Parliamentary Data]] (79.8% similar)
- [[2025-09-22/UPRPRC_ Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations_20250922|UPRPRC: Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations]] (79.1% similar)
- [[2025-09-23/SynParaSpeech_ Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding_20250923|SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding]] (78.9% similar)
- [[2025-09-24/LOTUSDIS_ A Thai far-field meeting corpus for robust conversational ASR_20250924|LOTUSDIS: A Thai far-field meeting corpus for robust conversational ASR]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Dialect Identification|Dialect Identification]], [[keywords/Automated Annotation|Automated Annotation]]
**⚡ Unique Technical**: [[keywords/Swiss German Speech Corpus|Swiss German Speech Corpus]], [[keywords/Spontaneous Speech|Spontaneous Speech]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19866v1 Announce Type: new 
Abstract: We present SwissGPC v1.0, the first mid-to-large-scale corpus of spontaneous Swiss German speech, developed to support research in ASR, TTS, dialect identification, and related fields. The dataset consists of links to talk shows and podcasts hosted on Schweizer Radio und Fernsehen and YouTube, which contain approximately 5400 hours of raw audio. After segmentation and weak annotation, nearly 5000 hours of speech were retained, covering the seven major Swiss German dialect regions alongside Standard German. We describe the corpus construction methodology, including an automated annotation pipeline, and provide statistics on dialect distribution, token counts, and segmentation characteristics. Unlike existing Swiss German speech corpora, which primarily feature controlled speech, this corpus captures natural, spontaneous conversations, making it a valuable resource for real-world speech applications.

## 📝 요약

SwissGPC v1.0은 자발적인 스위스 독일어 음성을 포함한 중대형 규모의 최초 코퍼스로, ASR, TTS, 방언 식별 연구를 지원합니다. 이 데이터셋은 약 5400시간의 원시 오디오를 포함하며, 스위스 라디오와 텔레비전, 유튜브의 토크쇼와 팟캐스트 링크로 구성되어 있습니다. 약 5000시간의 음성이 7개 주요 스위스 독일어 방언 지역과 표준 독일어를 포함하도록 세분화 및 약한 주석 작업을 거쳤습니다. 코퍼스 구축 방법론과 자동 주석 파이프라인을 설명하고, 방언 분포, 토큰 수, 세분화 특성에 대한 통계를 제공합니다. 기존의 통제된 스위스 독일어 음성 코퍼스와 달리, 자연스러운 자발적 대화를 담고 있어 실제 음성 응용에 유용한 자원입니다.

## 🎯 주요 포인트

- 1. SwissGPC v1.0은 자발적인 스위스 독일어 음성을 포함한 최초의 중대형 규모 코퍼스로, ASR, TTS, 방언 식별 등의 연구를 지원하기 위해 개발되었습니다.
- 2. 데이터셋은 Schweizer Radio und Fernsehen과 YouTube에 호스팅된 토크쇼와 팟캐스트 링크로 구성되어 있으며, 약 5400시간의 원시 오디오를 포함하고 있습니다.
- 3. 세분화 및 약한 주석 작업 후, 표준 독일어와 함께 스위스 독일어의 7개 주요 방언 지역을 포함하는 약 5000시간의 음성이 보존되었습니다.
- 4. 자동 주석 파이프라인을 포함한 코퍼스 구축 방법론을 설명하고, 방언 분포, 토큰 수, 세분화 특성에 대한 통계를 제공합니다.
- 5. 기존의 스위스 독일어 음성 코퍼스가 주로 통제된 음성을 특징으로 하는 것과 달리, 이 코퍼스는 자연스럽고 자발적인 대화를 포착하여 실제 음성 응용 프로그램에 유용한 자원이 됩니다.


---

*Generated on 2025-09-26 08:46:21*