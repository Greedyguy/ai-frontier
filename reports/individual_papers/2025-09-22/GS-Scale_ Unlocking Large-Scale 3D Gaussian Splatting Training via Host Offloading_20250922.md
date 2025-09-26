---
keywords:
  - 3D Gaussian Splatting
  - GPU Memory Optimization
  - Frustum Culling
  - Deferred Optimizer Update
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15645
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:04:31.475316",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "GPU Memory Optimization",
    "Frustum Culling",
    "Deferred Optimizer Update"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "GPU Memory Optimization": 0.82,
    "Frustum Culling": 0.77,
    "Deferred Optimizer Update": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3D Gaussian Rendering"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper, offering novel insights into graphics rendering.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "GPU Memory Optimization",
        "canonical": "GPU Memory Optimization",
        "aliases": [
          "GPU Memory Management"
        ],
        "category": "specific_connectable",
        "rationale": "Optimizing GPU memory is crucial for large-scale training, linking to broader discussions on hardware efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Frustum Culling",
        "canonical": "Frustum Culling",
        "aliases": [
          "View Frustum Culling"
        ],
        "category": "specific_connectable",
        "rationale": "Frustum culling is a key optimization technique in graphics, relevant for efficient rendering processes.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Deferred Optimizer Update",
        "canonical": "Deferred Optimizer Update",
        "aliases": [
          "Delayed Optimizer Update"
        ],
        "category": "unique_technical",
        "rationale": "This novel optimization strategy is specific to the paper's approach, enhancing training efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "training system",
      "memory demands",
      "consumer-grade GPUs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "GPU Memory Optimization",
      "resolved_canonical": "GPU Memory Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Frustum Culling",
      "resolved_canonical": "Frustum Culling",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Deferred Optimizer Update",
      "resolved_canonical": "Deferred Optimizer Update",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading

**Korean Title:** GS-Scale: 호스트 오프로딩을 통한 대규모 3D 가우시안 스플래팅 훈련의 잠재력 발휘

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15645.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15645](https://arxiv.org/abs/2509.15645)

## 🔗 유사한 논문
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (85.0% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (83.6% similar)
- [[2025-09-19/{\lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{\lambda}Scale: Enabling Fast Scaling for Serverless Large Language Model Inference]] (80.9% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (80.4% similar)
- [[2025-09-17/LamiGauss_ Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction_20250917|LamiGauss: Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/GPU Memory Optimization|GPU Memory Optimization]], [[keywords/Frustum Culling|Frustum Culling]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Deferred Optimizer Update|Deferred Optimizer Update]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15645v1 Announce Type: new 
Abstract: The advent of 3D Gaussian Splatting has revolutionized graphics rendering by delivering high visual quality and fast rendering speeds. However, training large-scale scenes at high quality remains challenging due to the substantial memory demands required to store parameters, gradients, and optimizer states, which can quickly overwhelm GPU memory. To address these limitations, we propose GS-Scale, a fast and memory-efficient training system for 3D Gaussian Splatting. GS-Scale stores all Gaussians in host memory, transferring only a subset to the GPU on demand for each forward and backward pass. While this dramatically reduces GPU memory usage, it requires frustum culling and optimizer updates to be executed on the CPU, introducing slowdowns due to CPU's limited compute and memory bandwidth. To mitigate this, GS-Scale employs three system-level optimizations: (1) selective offloading of geometric parameters for fast frustum culling, (2) parameter forwarding to pipeline CPU optimizer updates with GPU computation, and (3) deferred optimizer update to minimize unnecessary memory accesses for Gaussians with zero gradients. Our extensive evaluations on large-scale datasets demonstrate that GS-Scale significantly lowers GPU memory demands by 3.3-5.6x, while achieving training speeds comparable to GPU without host offloading. This enables large-scale 3D Gaussian Splatting training on consumer-grade GPUs; for instance, GS-Scale can scale the number of Gaussians from 4 million to 18 million on an RTX 4070 Mobile GPU, leading to 23-35% LPIPS (learned perceptual image patch similarity) improvement.

## 🔍 Abstract (한글 번역)

arXiv:2509.15645v1 발표 유형: 신규  
초록: 3D Gaussian Splatting의 출현은 높은 시각적 품질과 빠른 렌더링 속도를 제공함으로써 그래픽 렌더링에 혁신을 가져왔습니다. 그러나 고품질로 대규모 장면을 학습하는 것은 매개변수, 기울기 및 최적화기 상태를 저장하는 데 필요한 막대한 메모리 요구로 인해 여전히 어려운 과제입니다. 이러한 제한을 해결하기 위해, 우리는 3D Gaussian Splatting을 위한 빠르고 메모리 효율적인 학습 시스템인 GS-Scale을 제안합니다. GS-Scale은 모든 Gaussian을 호스트 메모리에 저장하고, 각 순방향 및 역방향 패스에 필요한 부분만 GPU로 전송합니다. 이는 GPU 메모리 사용량을 크게 줄이지만, 프러스텀 컬링과 최적화기 업데이트를 CPU에서 실행해야 하므로 CPU의 제한된 계산 및 메모리 대역폭으로 인해 속도가 느려질 수 있습니다. 이를 완화하기 위해 GS-Scale은 세 가지 시스템 수준 최적화를 사용합니다: (1) 빠른 프러스텀 컬링을 위한 기하학적 매개변수의 선택적 오프로딩, (2) CPU 최적화기 업데이트와 GPU 계산을 파이프라인화하기 위한 매개변수 전달, (3) 기울기가 0인 Gaussian에 대한 불필요한 메모리 접근을 최소화하기 위한 지연된 최적화기 업데이트. 대규모 데이터셋에 대한 우리의 광범위한 평가 결과, GS-Scale은 GPU 메모리 요구를 3.3-5.6배 크게 줄이면서, 호스트 오프로딩 없이도 GPU와 유사한 학습 속도를 달성함을 보여줍니다. 이는 소비자용 GPU에서 대규모 3D Gaussian Splatting 학습을 가능하게 합니다; 예를 들어, GS-Scale은 RTX 4070 모바일 GPU에서 Gaussian의 수를 400만 개에서 1800만 개로 확장할 수 있으며, 이는 23-35%의 LPIPS(학습된 지각 이미지 패치 유사도) 향상을 가져옵니다.

## 📝 요약

3D Gaussian Splatting은 그래픽 렌더링의 시각적 품질과 속도를 혁신했지만, 대규모 장면을 고품질로 학습하는 데는 여전히 높은 메모리 요구사항이 문제입니다. 이를 해결하기 위해, GS-Scale이라는 메모리 효율적인 3D Gaussian Splatting 학습 시스템을 제안합니다. GS-Scale은 모든 Gaussian을 호스트 메모리에 저장하고, 필요한 부분만 GPU로 전송하여 메모리 사용을 크게 줄입니다. CPU의 연산 한계를 극복하기 위해, GS-Scale은 세 가지 최적화를 도입합니다: (1) 빠른 프러스텀 컬링을 위한 선택적 오프로딩, (2) CPU 최적화 업데이트와 GPU 연산의 파이프라인 처리, (3) 불필요한 메모리 접근을 줄이기 위한 지연된 최적화 업데이트. 실험 결과, GS-Scale은 GPU 메모리 사용을 3.3-5.6배 줄이면서도 GPU 단독 사용과 유사한 학습 속도를 유지합니다. 이를 통해 소비자용 GPU에서도 대규모 3D Gaussian Splatting 학습이 가능해졌으며, 예를 들어 RTX 4070 Mobile GPU에서 Gaussian 수를 4백만에서 1천8백만으로 확장하여 LPIPS가 23-35% 개선되었습니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting은 높은 시각적 품질과 빠른 렌더링 속도로 그래픽 렌더링을 혁신했지만, 대규모 장면의 고품질 학습에는 여전히 높은 메모리 요구가 문제입니다.
- 2. GS-Scale은 모든 Gaussian을 호스트 메모리에 저장하고, 필요한 부분만 GPU로 전송하여 GPU 메모리 사용을 크게 줄이는 시스템을 제안합니다.
- 3. GS-Scale은 CPU의 계산 및 메모리 대역폭 제한으로 인한 속도 저하를 완화하기 위해 세 가지 시스템 수준 최적화를 사용합니다.
- 4. GS-Scale은 대규모 데이터셋 평가에서 GPU 메모리 요구를 3.3-5.6배 줄이면서도 GPU와 유사한 학습 속도를 달성합니다.
- 5. GS-Scale은 RTX 4070 Mobile GPU에서 Gaussian 수를 4백만에서 1천8백만으로 확장 가능하게 하여, LPIPS 개선을 23-35% 달성합니다.


---

*Generated on 2025-09-23 12:04:31*