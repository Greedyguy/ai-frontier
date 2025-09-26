---
keywords:
  - Geometric Mixture Classifier
  - Random Fourier Features
  - Multimodal Learning
  - Softmax Function
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16769
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:33:18.040778",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Geometric Mixture Classifier",
    "Random Fourier Features",
    "Multimodal Learning",
    "Softmax Function"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Geometric Mixture Classifier": 0.78,
    "Random Fourier Features": 0.75,
    "Multimodal Learning": 0.8,
    "Softmax Function": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Geometric Mixture Classifier",
        "canonical": "Geometric Mixture Classifier",
        "aliases": [
          "GMC"
        ],
        "category": "unique_technical",
        "rationale": "The Geometric Mixture Classifier is a novel model introduced in the paper, providing a unique approach to handling multimodal data.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Random Fourier Features",
        "canonical": "Random Fourier Features",
        "aliases": [
          "RFF"
        ],
        "category": "specific_connectable",
        "rationale": "Random Fourier Features are used for nonlinear mappings, connecting to other models using similar techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The paper addresses multimodal data, aligning with the trending concept of Multimodal Learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "softmax",
        "canonical": "Softmax Function",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Softmax is a fundamental concept in probabilistic models, linking to various machine learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "linear models",
      "high-capacity methods",
      "synthetic multimodal datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Geometric Mixture Classifier",
      "resolved_canonical": "Geometric Mixture Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Random Fourier Features",
      "resolved_canonical": "Random Fourier Features",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "softmax",
      "resolved_canonical": "Softmax Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Geometric Mixture Classifier (GMC): A Discriminative Per-Class Mixture of Hyperplanes

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16769.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16769](https://arxiv.org/abs/2509.16769)

## 🔗 유사한 논문
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (80.9% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.4% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.5% similar)
- [[2025-09-17/Graph-Regularized Learning of Gaussian Mixture Models_20250917|Graph-Regularized Learning of Gaussian Mixture Models]] (78.4% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Softmax Function|Softmax Function]]
**🔗 Specific Connectable**: [[keywords/Random Fourier Features|Random Fourier Features]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Geometric Mixture Classifier|Geometric Mixture Classifier]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16769v1 Announce Type: cross 
Abstract: Many real world categories are multimodal, with single classes occupying disjoint regions in feature space. Classical linear models (logistic regression, linear SVM) use a single global hyperplane and perform poorly on such data, while high-capacity methods (kernel SVMs, deep nets) fit multimodal structure but at the expense of interpretability, heavier tuning, and higher computational cost. We propose the Geometric Mixture Classifier (GMC), a discriminative model that represents each class as a mixture of hyperplanes. Within each class, GMC combines plane scores via a temperature-controlled soft-OR (log-sum-exp), smoothly approximating the max; across classes, standard softmax yields probabilistic posteriors. GMC optionally uses Random Fourier Features (RFF) for nonlinear mappings while keeping inference linear in the number of planes and features. Our practical training recipe: geometry-aware k-means initialization, silhouette-based plane budgeting, alpha annealing, usage-aware L2 regularization, label smoothing, and early stopping, makes GMC plug-and-play. Across synthetic multimodal datasets (moons, circles, blobs, spirals) and tabular/image benchmarks (iris, wine, WDBC, digits), GMC consistently outperforms linear baselines and k-NN, is competitive with RBF-SVM, Random Forests, and small MLPs, and provides geometric introspection via per-plane and class responsibility visualizations. Inference scales linearly in planes and features, making GMC CPU-friendly, with single-digit microsecond latency per example, often faster than RBF-SVM and compact MLPs. Post-hoc temperature scaling reduces ECE from about 0.06 to 0.02. GMC thus strikes a favorable balance of accuracy, interpretability, and efficiency: it is more expressive than linear models and lighter, more transparent, and faster than kernel or deep models.

## 📝 요약

Geometric Mixture Classifier (GMC)는 각 클래스를 여러 초평면의 혼합으로 표현하는 판별 모델로, 다중 모달 구조를 효과적으로 처리합니다. GMC는 클래스 내에서 온도 조절된 soft-OR를 사용해 평면 점수를 결합하고, 클래스 간에는 소프트맥스를 통해 확률적 사후 확률을 제공합니다. 랜덤 푸리에 특징을 사용해 비선형 매핑을 지원하면서도 추론은 선형적으로 유지합니다. 실용적인 학습 방법으로는 기하학적 k-평균 초기화, 실루엣 기반 평면 예산, 알파 어닐링, 사용 인식 L2 정규화, 라벨 스무딩, 조기 중단 등이 포함됩니다. GMC는 합성 및 실제 데이터셋에서 선형 모델과 k-NN을 능가하며, RBF-SVM, 랜덤 포레스트, 소형 MLP와 경쟁력을 보입니다. 또한, 해석 가능성과 효율성을 제공하며, 추론이 CPU 친화적이고 빠릅니다. GMC는 정확성, 해석 가능성, 효율성의 균형을 잘 맞추어 선형 모델보다 표현력이 뛰어나고, 커널 및 심층 모델보다 가볍고 투명하며 빠릅니다.

## 🎯 주요 포인트

- 1. Geometric Mixture Classifier (GMC)는 각 클래스를 여러 초평면의 혼합으로 표현하여 멀티모달 구조를 효과적으로 모델링합니다.
- 2. GMC는 랜덤 푸리에 특징(RFF)을 사용하여 비선형 매핑을 수행하면서도 추론을 선형적으로 유지합니다.
- 3. GMC는 다양한 합성 멀티모달 데이터셋과 표준 벤치마크에서 선형 모델과 k-NN을 능가하며, RBF-SVM, 랜덤 포레스트, 소형 MLP와 경쟁력 있는 성능을 보입니다.
- 4. GMC는 각 초평면과 클래스의 책임 시각화를 통해 기하학적 통찰을 제공하며, CPU 친화적이고 예제 당 마이크로초 단위의 낮은 지연 시간을 자랑합니다.
- 5. 사후 온도 조정을 통해 ECE를 약 0.06에서 0.02로 줄이며, 정확성, 해석 가능성, 효율성의 균형을 잘 맞춥니다.


---

*Generated on 2025-09-23 23:33:18*