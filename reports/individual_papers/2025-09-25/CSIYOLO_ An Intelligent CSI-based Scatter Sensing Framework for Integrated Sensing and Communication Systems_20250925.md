---
keywords:
  - Integrated Sensing and Communication
  - CSI-based Scatter Localization
  - You Only Look Once
  - Noise Injection Training
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19335
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:25:47.221418",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Integrated Sensing and Communication",
    "CSI-based Scatter Localization",
    "You Only Look Once",
    "Noise Injection Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Integrated Sensing and Communication": 0.78,
    "CSI-based Scatter Localization": 0.77,
    "You Only Look Once": 0.8,
    "Noise Injection Training": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Integrated Sensing and Communication",
        "canonical": "Integrated Sensing and Communication",
        "aliases": [
          "ISAC"
        ],
        "category": "unique_technical",
        "rationale": "It represents a novel approach combining sensing and communication, crucial for linking related research in next-generation systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "CSI-based Scatter Localization",
        "canonical": "CSI-based Scatter Localization",
        "aliases": [
          "Channel State Information Scatter Localization"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's contribution and connects to advanced localization methods in communication systems.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "You Only Look Once architectures",
        "canonical": "You Only Look Once",
        "aliases": [
          "YOLO"
        ],
        "category": "specific_connectable",
        "rationale": "YOLO is a well-known architecture in computer vision, facilitating connections to similar detection frameworks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Noise Injection Training Strategy",
        "canonical": "Noise Injection Training",
        "aliases": [
          "Noise Injection"
        ],
        "category": "unique_technical",
        "rationale": "This strategy enhances robustness and can link to other works focusing on training methodologies under noisy conditions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Integrated Sensing and Communication",
      "resolved_canonical": "Integrated Sensing and Communication",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CSI-based Scatter Localization",
      "resolved_canonical": "CSI-based Scatter Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "You Only Look Once architectures",
      "resolved_canonical": "You Only Look Once",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Noise Injection Training Strategy",
      "resolved_canonical": "Noise Injection Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CSIYOLO: An Intelligent CSI-based Scatter Sensing Framework for Integrated Sensing and Communication Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19335.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19335](https://arxiv.org/abs/2509.19335)

## 🔗 유사한 논문
- [[2025-09-19/FAWN_ A MultiEncoder Fusion-Attention Wave Network for Integrated Sensing and Communication Indoor Scene Inference_20250919|FAWN: A MultiEncoder Fusion-Attention Wave Network for Integrated Sensing and Communication Indoor Scene Inference]] (78.8% similar)
- [[2025-09-19/Secure Short-Packet Communications for RIS-Assisted AAV Networks_20250919|Secure Short-Packet Communications for RIS-Assisted AAV Networks]] (78.4% similar)
- [[2025-09-17/Multi-robot Multi-source Localization in Complex Flows with Physics-Preserving Environment Models_20250917|Multi-robot Multi-source Localization in Complex Flows with Physics-Preserving Environment Models]] (77.6% similar)
- [[2025-09-22/Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment_20250922|Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment]] (77.6% similar)
- [[2025-09-19/A Software-Defined Radio Testbed for Distributed LiDAR Point Cloud Sharing with IEEE 802.11p in V2V Networks_20250919|A Software-Defined Radio Testbed for Distributed LiDAR Point Cloud Sharing with IEEE 802.11p in V2V Networks]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/You Only Look Once|You Only Look Once]]
**⚡ Unique Technical**: [[keywords/Integrated Sensing and Communication|Integrated Sensing and Communication]], [[keywords/CSI-based Scatter Localization|CSI-based Scatter Localization]], [[keywords/Noise Injection Training|Noise Injection Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19335v1 Announce Type: cross 
Abstract: ISAC is regarded as a promising technology for next-generation communication systems, enabling simultaneous data transmission and target sensing. Among various tasks in ISAC, scatter sensing plays a crucial role in exploiting the full potential of ISAC and supporting applications such as autonomous driving and low-altitude economy. However, most existing methods rely on either waveform and hardware modifications or traditional signal processing schemes, leading to poor compatibility with current communication systems and limited sensing accuracy. To address these challenges, we propose CSIYOLO, a framework that performs scatter localization only using estimated CSI from a single base station-user equipment pair. This framework comprises two main components: anchor-based scatter parameter detection and CSI-based scatter localization. First, by formulating scatter parameter extraction as an image detection problem, we propose an anchor-based scatter parameter detection method inspired by You Only Look Once architectures. After that, a CSI-based localization algorithm is derived to determine scatter locations with extracted parameters. Moreover, to improve localization accuracy and implementation efficiency, we design an extendable network structure with task-oriented optimizations, enabling multi-scale anchor detection and better adaptation to CSI characteristics. A noise injection training strategy is further designed to enhance robustness against channel estimation errors. Since the proposed framework operates solely on estimated CSI without modifying waveforms or signal processing pipelines, it can be seamlessly integrated into existing communication systems as a plugin. Experiments show that our proposed method can significantly outperform existing methods in scatter localization accuracy with relatively low complexities under varying numbers of scatters and estimation errors.

## 📝 요약

ISAC 기술은 차세대 통신 시스템에서 데이터 전송과 목표물 감지를 동시에 가능하게 하는 유망한 기술로 주목받고 있습니다. 특히, 산란체 감지는 자율주행 및 저고도 경제와 같은 응용 분야를 지원하는 데 중요한 역할을 합니다. 기존 방법들은 주로 파형 및 하드웨어 수정이나 전통적인 신호 처리 방식에 의존하여 현재 통신 시스템과의 호환성이 낮고 감지 정확도가 제한적입니다. 이를 해결하기 위해, 우리는 단일 기지국-사용자 장비 쌍의 추정된 CSI만을 사용하여 산란체 위치를 파악하는 CSIYOLO 프레임워크를 제안합니다. 이 프레임워크는 앵커 기반의 산란체 매개변수 감지와 CSI 기반의 산란체 위치 추정으로 구성됩니다. 제안된 방법은 기존 통신 시스템에 플러그인으로 통합될 수 있으며, 실험 결과, 다양한 산란체 수와 추정 오류 하에서도 기존 방법보다 높은 정확도로 산란체 위치를 파악할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. ISAC는 차세대 통신 시스템에서 데이터 전송과 목표물 감지를 동시에 가능하게 하는 유망한 기술로 간주됩니다.
- 2. 기존 방법들은 파형 및 하드웨어 수정이나 전통적인 신호 처리 방식에 의존하여 현재 통신 시스템과의 호환성이 낮고 감지 정확도가 제한적입니다.
- 3. CSIYOLO는 단일 기지국-사용자 장비 쌍의 추정된 CSI만을 사용하여 산란체 위치를 파악하는 프레임워크로, 앵커 기반 산란 매개변수 감지와 CSI 기반 산란 위치 추정으로 구성됩니다.
- 4. 제안된 프레임워크는 파형이나 신호 처리 파이프라인을 수정하지 않고 추정된 CSI만으로 작동하여 기존 통신 시스템에 플러그인으로 원활하게 통합될 수 있습니다.
- 5. 실험 결과, 제안된 방법은 다양한 산란체 수와 추정 오류 하에서도 산란체 위치 추정 정확도에서 기존 방법보다 우수한 성능을 보입니다.


---

*Generated on 2025-09-25 15:25:47*