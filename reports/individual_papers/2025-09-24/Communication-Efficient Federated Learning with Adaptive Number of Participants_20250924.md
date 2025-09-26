<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:27:31.910504",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Intelligent Selection of Participants",
    "Transformer",
    "Gradient Compression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Intelligent Selection of Participants": 0.8,
    "Transformer": 0.78,
    "Gradient Compression": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a central theme of the paper and connects to many related works in decentralized training.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Intelligent Selection of Participants",
        "canonical": "Intelligent Selection of Participants",
        "aliases": [
          "ISP"
        ],
        "category": "unique_technical",
        "rationale": "ISP is a novel mechanism introduced in the paper, offering a unique approach to optimizing client participation in federated learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision Transformers",
        "canonical": "Transformer",
        "aliases": [
          "Vision Transformer"
        ],
        "category": "broad_technical",
        "rationale": "Vision Transformers are a specific application of Transformers, linking to broader discussions on deep learning models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gradient Compression",
        "canonical": "Gradient Compression",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Gradient Compression is a technique to reduce communication costs in federated learning, relevant to the paper's focus.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "communication efficiency",
      "client selection strategies"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Intelligent Selection of Participants",
      "resolved_canonical": "Intelligent Selection of Participants",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gradient Compression",
      "resolved_canonical": "Gradient Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Communication-Efficient Federated Learning with Adaptive Number of Participants

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.13803.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2508.13803](https://arxiv.org/abs/2508.13803)

## 🔗 유사한 논문
- [[2025-09-23/Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation_ A Stagewise Decision-Making Methodology_20250923|Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation: A Stagewise Decision-Making Methodology]] (87.3% similar)
- [[2025-09-24/FedFiTS_ Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI_20250924|FedFiTS: Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI]] (86.9% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (84.5% similar)
- [[2025-09-23/Asynchronous Federated Learning_ A Scalable Approach for Decentralized Machine Learning_20250923|Asynchronous Federated Learning: A Scalable Approach for Decentralized Machine Learning]] (84.4% similar)
- [[2025-09-23/FedEL_ Federated Elastic Learning for Heterogeneous Devices_20250923|FedEL: Federated Elastic Learning for Heterogeneous Devices]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Gradient Compression|Gradient Compression]]
**⚡ Unique Technical**: [[keywords/Intelligent Selection of Participants|Intelligent Selection of Participants]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.13803v2 Announce Type: replace 
Abstract: Rapid scaling of deep learning models has enabled performance gains across domains, yet it introduced several challenges. Federated Learning (FL) has emerged as a promising framework to address these concerns by enabling decentralized training. Nevertheless, communication efficiency remains a key bottleneck in FL, particularly under heterogeneous and dynamic client participation. Existing methods, such as FedAvg and FedProx, or other approaches, including client selection strategies, attempt to mitigate communication costs. However, the problem of choosing the number of clients in a training round remains extremely underexplored. We introduce Intelligent Selection of Participants (ISP), an adaptive mechanism that dynamically determines the optimal number of clients per round to enhance communication efficiency without compromising model accuracy. We validate the effectiveness of ISP across diverse setups, including vision transformers, real-world ECG classification, and training with gradient compression. Our results show consistent communication savings of up to 30\% without losing the final quality. Applying ISP to different real-world ECG classification setups highlighted the selection of the number of clients as a separate task of federated learning.

## 📝 요약

이 논문은 연합 학습(FL)에서의 통신 효율성을 개선하기 위해 제안된 새로운 메커니즘인 ISP(Intelligent Selection of Participants)를 소개합니다. 기존의 방법들이 통신 비용을 줄이려 했지만, 각 학습 라운드에서 참여할 클라이언트 수를 결정하는 문제는 충분히 탐구되지 않았습니다. ISP는 라운드별 최적의 클라이언트 수를 동적으로 결정하여 통신 효율성을 높이면서도 모델 정확도를 유지합니다. 다양한 환경에서 ISP의 효과를 검증한 결과, 최대 30%의 통신 절감 효과를 보였으며, 특히 ECG 분류와 같은 실제 응용에서 클라이언트 수 선택이 중요한 과제로 부각되었습니다.

## 🎯 주요 포인트

- 1. 연합 학습(Federated Learning, FL)은 분산형 학습을 가능하게 하여 딥러닝 모델의 성능 향상을 지원하지만, 통신 효율성은 여전히 주요 병목 현상으로 남아 있습니다.
- 2. 기존 방법들은 통신 비용을 줄이기 위해 노력하고 있지만, 학습 라운드에서 클라이언트 수를 선택하는 문제는 거의 탐구되지 않았습니다.
- 3. ISP(Intelligent Selection of Participants)는 라운드당 최적의 클라이언트 수를 동적으로 결정하여 통신 효율성을 향상시키는 적응형 메커니즘입니다.
- 4. ISP는 다양한 설정에서 최대 30%의 통신 비용 절감을 이루면서도 모델의 최종 품질을 유지하는 데 성공했습니다.
- 5. ISP를 ECG 분류와 같은 실제 사례에 적용한 결과, 클라이언트 수 선택이 연합 학습의 별도 과업임을 강조했습니다.


---

*Generated on 2025-09-24 15:27:31*