---
keywords:
  - X-ray Computed Laminography
  - Sparse-View Reconstruction
  - Gaussian Splatting
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:52:55.796984",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "X-ray Computed Laminography",
    "Sparse-View Reconstruction",
    "Gaussian Splatting"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "X-ray Computed Laminography": 0.78,
    "Sparse-View Reconstruction": 0.75,
    "Gaussian Splatting": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# LamiGauss: Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction

**Korean Title:** LamiGauss: 희소 뷰 X선 라미노그래피 재구성을 위한 방사형 가우시안 기법

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/X-ray Computed Laminography|X-ray Computed Laminography]], [[keywords/Sparse-View Reconstruction|Sparse-View Reconstruction]], [[keywords/Gaussian Splatting|Gaussian Splatting]]

## 🔗 유사한 논문
- [[Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (81.0% similar)
- [[MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (79.3% similar)
- [[Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (78.1% similar)
- [[Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (78.0% similar)
- [[Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (77.9% similar)

## 📋 저자 정보

**Authors:** Chu Chen, Ander Biguri, Jean-Michel Morel, Raymond H. Chan, Carola-Bibiane Schönlieb, Jizhou Li

## 📄 Abstract (원문)

X-ray Computed Laminography (CL) is essential for non-destructive inspection
of plate-like structures in applications such as microchips and composite
battery materials, where traditional computed tomography (CT) struggles due to
geometric constraints. However, reconstructing high-quality volumes from
laminographic projections remains challenging, particularly under highly
sparse-view acquisition conditions. In this paper, we propose a reconstruction
algorithm, namely LamiGauss, that combines Gaussian Splatting radiative
rasterization with a dedicated detector-to-world transformation model
incorporating the laminographic tilt angle. LamiGauss leverages an
initialization strategy that explicitly filters out common laminographic
artifacts from the preliminary reconstruction, preventing redundant Gaussians
from being allocated to false structures and thereby concentrating model
capacity on representing the genuine object. Our approach effectively optimizes
directly from sparse projections, enabling accurate and efficient
reconstruction with limited data. Extensive experiments on both synthetic and
real datasets demonstrate the effectiveness and superiority of the proposed
method over existing techniques. LamiGauss uses only 3$\%$ of full views to
achieve superior performance over the iterative method optimized on a full
dataset.

## 🔍 Abstract (한글 번역)

엑스레이 컴퓨터 라미노그래피(X-ray Computed Laminography, CL)는 전통적인 컴퓨터 단층촬영(CT)이 기하학적 제약으로 인해 어려움을 겪는 마이크로칩 및 복합 배터리 재료와 같은 응용 분야에서 판상 구조의 비파괴 검사를 위해 필수적입니다. 그러나 라미노그래픽 투영으로부터 고품질의 볼륨을 재구성하는 것은 특히 매우 희소한 뷰 획득 조건에서 여전히 도전 과제입니다. 본 논문에서는 라미노그래픽 기울기 각도를 통합한 전용 검출기-세계 변환 모델과 가우시안 스플래팅 방사 래스터화를 결합한 재구성 알고리즘인 LamiGauss를 제안합니다. LamiGauss는 초기 재구성에서 일반적인 라미노그래픽 아티팩트를 명시적으로 필터링하는 초기화 전략을 활용하여 잘못된 구조에 중복된 가우시안이 할당되는 것을 방지하고, 모델 용량을 실제 객체를 표현하는 데 집중시킵니다. 우리의 접근 방식은 희소한 투영으로부터 직접 최적화하여 제한된 데이터로도 정확하고 효율적인 재구성을 가능하게 합니다. 합성 및 실제 데이터 세트에 대한 광범위한 실험을 통해 제안된 방법이 기존 기술보다 효과적이고 우수함을 입증합니다. LamiGauss는 전체 데이터 세트에서 최적화된 반복 방법보다 우수한 성능을 달성하기 위해 전체 뷰의 3%만을 사용합니다.

## 📝 요약

X-ray Computed Laminography (CL)는 전통적인 CT가 기하학적 제약으로 어려움을 겪는 미세칩 및 복합 배터리 소재의 비파괴 검사에 필수적입니다. 본 논문에서는 LamiGauss라는 알고리즘을 제안하여, 가우시안 스플래팅 방사 래스터화와 라미노그래픽 기울기 각도를 포함한 변환 모델을 결합하여 고품질 볼륨 재구성을 수행합니다. 초기화 전략을 통해 일반적인 라미노그래픽 아티팩트를 제거하고, 진정한 구조에 모델 용량을 집중시킵니다. 이 방법은 희소한 투영 데이터로부터 직접 최적화하여 정확하고 효율적인 재구성을 가능하게 합니다. 실험 결과, LamiGauss는 전체 데이터셋의 3%만 사용해도 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. X선 컴퓨티드 라미노그래피(CL)는 전통적인 컴퓨티드 토모그래피(CT)가 기하학적 제약으로 어려움을 겪는 미세칩 및 복합 배터리 소재와 같은 판형 구조의 비파괴 검사에 필수적입니다.

- 2. LamiGauss는 라미노그래픽 투영에서 고품질 볼륨을 재구성하기 위해 가우시안 스플래팅 방사 래스터화와 라미노그래픽 기울기 각도를 포함한 전용 검출기-세계 변환 모델을 결합한 알고리즘입니다.

- 3. LamiGauss는 초기화 전략을 통해 일반적인 라미노그래픽 아티팩트를 제거하고, 잘못된 구조에 중복 가우시안이 할당되는 것을 방지하여 모델 용량을 실제 객체 표현에 집중시킵니다.

- 4. 제안된 방법은 제한된 데이터로도 정확하고 효율적인 재구성을 가능하게 하며, 실험 결과 기존 기술보다 우수한 성능을 입증했습니다.

- 5. LamiGauss는 전체 데이터셋을 최적화한 반복적 방법보다 3%의 전체 뷰만 사용하여 우수한 성능을 달성합니다.

---

*Generated on 2025-09-20 09:28:16*