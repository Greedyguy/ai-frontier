---
keywords:
  - Graph Neural Network
  - B-spline Surface Reconstruction
  - Point Cloud
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16050
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:18:46.261831",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "B-spline Surface Reconstruction",
    "Point Cloud"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.79,
    "B-spline Surface Reconstruction": 0.78,
    "Point Cloud": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Convolutional Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GCN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the proposed method for surface reconstruction, enhancing connectivity with existing literature.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "B-spline reconstruction",
        "canonical": "B-spline Surface Reconstruction",
        "aliases": [
          "B-spline",
          "Spline Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "B-spline techniques are specifically highlighted for their smoothening properties in noisy data, offering unique insights into surface reconstruction.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Point Cloud",
        "canonical": "Point Cloud",
        "aliases": [
          "3D Point Cloud"
        ],
        "category": "broad_technical",
        "rationale": "Point clouds are fundamental to the study, providing a basis for linking various 3D vision applications.",
        "novelty_score": 0.31,
        "connectivity_score": 0.79,
        "specificity_score": 0.68,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "surface reconstruction",
      "control points"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Convolutional Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "B-spline reconstruction",
      "resolved_canonical": "B-spline Surface Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Point Cloud",
      "resolved_canonical": "Point Cloud",
      "decision": "linked",
      "scores": {
        "novelty": 0.31,
        "connectivity": 0.79,
        "specificity": 0.68,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Graph-based Point Cloud Surface Reconstruction using B-Splines

**Korean Title:** B-스플라인을 이용한 그래프 기반 포인트 클라우드 표면 재구성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16050.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16050](https://arxiv.org/abs/2509.16050)

## 🔗 유사한 논문
- [[2025-09-22/A PCA Based Model for Surface Reconstruction from Incomplete Point Clouds_20250922|A PCA Based Model for Surface Reconstruction from Incomplete Point Clouds]] (85.1% similar)
- [[2025-09-22/MoAngelo_ Motion-Aware Neural Surface Reconstruction for Dynamic Scenes_20250922|MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes]] (80.8% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (80.1% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (79.1% similar)
- [[2025-09-22/FloorSAM_ SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion_20250922|FloorSAM: SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Point Cloud|Point Cloud]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/B-spline Surface Reconstruction|B-spline Surface Reconstruction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16050v1 Announce Type: new 
Abstract: Generating continuous surfaces from discrete point cloud data is a fundamental task in several 3D vision applications. Real-world point clouds are inherently noisy due to various technical and environmental factors. Existing data-driven surface reconstruction algorithms rely heavily on ground truth normals or compute approximate normals as an intermediate step. This dependency makes them extremely unreliable for noisy point cloud datasets, even if the availability of ground truth training data is ensured, which is not always the case. B-spline reconstruction techniques provide compact surface representations of point clouds and are especially known for their smoothening properties. However, the complexity of the surfaces approximated using B-splines is directly influenced by the number and location of the spline control points. Existing spline-based modeling methods predict the locations of a fixed number of control points for a given point cloud, which makes it very difficult to match the complexity of its underlying surface. In this work, we develop a Dictionary-Guided Graph Convolutional Network-based surface reconstruction strategy where we simultaneously predict both the location and the number of control points for noisy point cloud data to generate smooth surfaces without the use of any point normals. We compare our reconstruction method with several well-known as well as recent baselines by employing widely-used evaluation metrics, and demonstrate that our method outperforms all of them both qualitatively and quantitatively.

## 🔍 Abstract (한글 번역)

arXiv:2509.16050v1 발표 유형: 새로운 
초록: 이산 점군 데이터로부터 연속적인 표면을 생성하는 것은 여러 3D 비전 응용 분야에서 기본적인 작업입니다. 실제 세계의 점군은 다양한 기술적 및 환경적 요인으로 인해 본질적으로 노이즈가 많습니다. 기존의 데이터 기반 표면 재구성 알고리즘은 주로 실제 법선에 의존하거나 중간 단계로 근사 법선을 계산합니다. 이러한 의존성은 실제 학습 데이터의 가용성이 보장되더라도, 노이즈가 많은 점군 데이터셋에 대해 매우 신뢰할 수 없게 만듭니다. B-스플라인 재구성 기법은 점군의 압축된 표면 표현을 제공하며, 특히 매끄러운 특성으로 잘 알려져 있습니다. 그러나 B-스플라인을 사용하여 근사화된 표면의 복잡성은 스플라인 제어점의 수와 위치에 직접적으로 영향을 받습니다. 기존의 스플라인 기반 모델링 방법은 주어진 점군에 대해 고정된 수의 제어점 위치를 예측하며, 이는 기본 표면의 복잡성을 맞추기 매우 어렵게 만듭니다. 본 연구에서는 사전 사전(Dictionary-Guided) 그래프 합성곱 신경망 기반의 표면 재구성 전략을 개발하여, 점 법선을 사용하지 않고도 노이즈가 많은 점군 데이터에 대해 매끄러운 표면을 생성하기 위해 제어점의 위치와 수를 동시에 예측합니다. 우리는 널리 사용되는 평가 지표를 사용하여 여러 잘 알려진 및 최신 기준선과 우리의 재구성 방법을 비교하고, 우리의 방법이 질적 및 양적으로 모두 그들을 능가함을 입증합니다.

## 📝 요약

이 논문은 잡음이 많은 점군 데이터에서 연속적인 표면을 생성하는 새로운 방법론을 제안합니다. 기존의 표면 재구성 알고리즘은 주로 점의 법선을 필요로 하며, 이는 잡음이 많은 데이터셋에서는 신뢰성이 떨어집니다. 본 연구에서는 Dictionary-Guided Graph Convolutional Network를 활용하여 점의 법선 없이도 제어점의 위치와 개수를 동시에 예측하여 매끄러운 표면을 생성합니다. 제안된 방법은 여러 평가 지표를 통해 기존의 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 연속적인 표면을 생성하는 것은 3D 비전 응용에서 중요한 과제이며, 실제 점군 데이터는 기술적 및 환경적 요인으로 인해 본질적으로 노이즈가 많습니다.
- 2. 기존의 데이터 기반 표면 재구성 알고리즘은 주로 정확한 법선 벡터에 의존하지만, 이는 노이즈가 많은 점군 데이터셋에서는 신뢰성이 떨어집니다.
- 3. B-스플라인 재구성 기술은 점군의 매끄러운 표면 표현을 제공하지만, 스플라인 제어점의 수와 위치에 따라 표면의 복잡성이 결정됩니다.
- 4. 본 연구에서는 사전 정의된 법선 벡터 없이 노이즈가 많은 점군 데이터에 대해 제어점의 위치와 수를 동시에 예측하여 매끄러운 표면을 생성하는 Dictionary-Guided Graph Convolutional Network 기반의 표면 재구성 전략을 개발했습니다.
- 5. 제안된 방법은 여러 평가 기준을 사용한 비교 실험에서 기존의 여러 기법들보다 질적 및 양적으로 우수한 성능을 보였습니다.


---

*Generated on 2025-09-23 12:18:46*