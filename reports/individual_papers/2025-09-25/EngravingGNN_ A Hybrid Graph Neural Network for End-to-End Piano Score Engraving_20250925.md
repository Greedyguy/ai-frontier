---
keywords:
  - Graph Neural Network
  - Automatic Music Engraving
  - Symbolic Music Processing
  - Multi-task Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19412
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:35:26.381580",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Automatic Music Engraving",
    "Symbolic Music Processing",
    "Multi-task Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Automatic Music Engraving": 0.78,
    "Symbolic Music Processing": 0.8,
    "Multi-task Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's approach, linking to existing research on neural networks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Music Engraving",
        "canonical": "Automatic Music Engraving",
        "aliases": [
          "Score Engraving"
        ],
        "category": "unique_technical",
        "rationale": "Defines the primary application domain of the research, offering a unique link to music processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Symbolic Music Processing",
        "canonical": "Symbolic Music Processing",
        "aliases": [
          "Symbolic Music"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader field of music information retrieval and processing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-task Learning",
        "canonical": "Multi-task Learning",
        "aliases": [
          "Multi-task GNN"
        ],
        "category": "broad_technical",
        "rationale": "Highlights the methodological approach, linking to machine learning strategies.",
        "novelty_score": 0.48,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "evaluation",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Music Engraving",
      "resolved_canonical": "Automatic Music Engraving",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Symbolic Music Processing",
      "resolved_canonical": "Symbolic Music Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-task Learning",
      "resolved_canonical": "Multi-task Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# EngravingGNN: A Hybrid Graph Neural Network for End-to-End Piano Score Engraving

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19412.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19412](https://arxiv.org/abs/2509.19412)

## 🔗 유사한 논문
- [[2025-09-23/Etude_ Piano Cover Generation with a Three-Stage Approach -- Extract, strucTUralize, and DEcode_20250923|Etude: Piano Cover Generation with a Three-Stage Approach -- Extract, strucTUralize, and DEcode]] (84.1% similar)
- [[2025-09-23/Barwise Section Boundary Detection in Symbolic Music Using Convolutional Neural Networks_20250923|Barwise Section Boundary Detection in Symbolic Music Using Convolutional Neural Networks]] (83.4% similar)
- [[2025-09-23/PerceiverS_ A Multi-Scale Perceiver with Effective Segmentation for Long-Term Expressive Symbolic Music Generation_20250923|PerceiverS: A Multi-Scale Perceiver with Effective Segmentation for Long-Term Expressive Symbolic Music Generation]] (83.3% similar)
- [[2025-09-19/Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation_20250919|Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation]] (83.1% similar)
- [[2025-09-23/SongPrep_ A Preprocessing Framework and End-to-end Model for Full-song Structure Parsing and Lyrics Transcription_20250923|SongPrep: A Preprocessing Framework and End-to-end Model for Full-song Structure Parsing and Lyrics Transcription]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-task Learning|Multi-task Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Symbolic Music Processing|Symbolic Music Processing]]
**⚡ Unique Technical**: [[keywords/Automatic Music Engraving|Automatic Music Engraving]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19412v1 Announce Type: cross 
Abstract: This paper focuses on automatic music engraving, i.e., the creation of a humanly-readable musical score from musical content. This step is fundamental for all applications that include a human player, but it remains a mostly unexplored topic in symbolic music processing. In this work, we formalize the problem as a collection of interdependent subtasks, and propose a unified graph neural network (GNN) framework that targets the case of piano music and quantized symbolic input. Our method employs a multi-task GNN to jointly predict voice connections, staff assignments, pitch spelling, key signature, stem direction, octave shifts, and clef signs. A dedicated postprocessing pipeline generates print-ready MusicXML/MEI outputs. Comprehensive evaluation on two diverse piano corpora (J-Pop and DCML Romantic) demonstrates that our unified model achieves good accuracy across all subtasks, compared to existing systems that only specialize in specific subtasks. These results indicate that a shared GNN encoder with lightweight task-specific decoders in a multi-task setting offers a scalable and effective solution for automatic music engraving.

## 📝 요약

이 논문은 자동 음악 조판, 즉 음악 콘텐츠로부터 사람이 읽을 수 있는 악보를 생성하는 문제를 다룹니다. 이는 상징적 음악 처리에서 거의 탐구되지 않은 주제입니다. 저자들은 이 문제를 상호 의존적인 여러 하위 작업의 집합으로 공식화하고, 피아노 음악과 양자화된 상징적 입력을 대상으로 하는 통합 그래프 신경망(GNN) 프레임워크를 제안합니다. 이 방법은 다중 작업 GNN을 사용하여 음성 연결, 오선지 할당, 음 높이 표기, 조표, 음줄 방향, 옥타브 이동, 음자리표를 예측합니다. 또한, 전용 후처리 파이프라인을 통해 인쇄 가능한 MusicXML/MEI 출력물을 생성합니다. J-Pop과 DCML Romantic 두 가지 피아노 코퍼스를 대상으로 한 평가에서, 제안된 모델은 모든 하위 작업에서 기존 시스템보다 높은 정확도를 보였습니다. 이는 다중 작업 환경에서 경량의 작업별 디코더를 사용하는 공유 GNN 인코더가 자동 음악 조판에 효과적이고 확장 가능한 솔루션임을 시사합니다.

## 🎯 주요 포인트

- 1. 이 논문은 자동 음악 조판, 즉 음악 콘텐츠로부터 사람이 읽을 수 있는 악보를 생성하는 과정에 중점을 둡니다.
- 2. 피아노 음악과 양자화된 기호 입력을 대상으로 하는 통합 그래프 신경망(GNN) 프레임워크를 제안합니다.
- 3. 제안된 방법은 다중 작업 GNN을 사용하여 음성 연결, 오선지 할당, 음 높이 철자, 조표, 음줄 방향, 옥타브 이동, 음자리표를 공동으로 예측합니다.
- 4. 전용 후처리 파이프라인을 통해 인쇄 가능한 MusicXML/MEI 출력물을 생성합니다.
- 5. 두 가지 다양한 피아노 코퍼스(J-Pop 및 DCML Romantic)에 대한 종합 평가 결과, 제안된 모델이 모든 하위 작업에서 기존 시스템보다 높은 정확도를 달성함을 보여줍니다.


---

*Generated on 2025-09-25 15:35:26*