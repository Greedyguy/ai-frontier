---
keywords:
  - Diffusion Models
  - Transformer Architecture
  - Block-Wise Caching
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 23:00:34.251475",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Transformer Architecture",
    "Block-Wise Caching"
  ],
  "rejected_keywords": [
    "Generative Models"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.9,
    "Transformer Architecture": 0.85,
    "Block-Wise Caching": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching

**Korean Title:** BWCache: 블록 단위 캐싱을 통한 비디오 확산 변환기의 가속화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Transformers]], [[keywords/Transformer Architecture|Transformer Architecture]]
**⚡ Unique Technical**: [[keywords/Block-Wise Caching|Block-Wise Caching]]

## 🔗 유사한 논문
- [[SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff Accelerating Diffusion Model Inference with Self-Speculation]] (81.3% similar)
- [[FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (80.8% similar)
- [[WorldForge_ Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (80.4% similar)
- [[Dense Video Understanding with Gated Residual Tokenization_20250917|Dense Video Understanding with Gated Residual Tokenization]] (79.1% similar)
- [[Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations_20250918|Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations]] (79.0% similar)

## 📋 저자 정보

**Authors:** Hanshuai Cui, Zhiqing Tang, Zhifei Xu, Zhi Yao, Wenyi Zeng, Weijia Jia

## 📄 Abstract (원문)

Recent advancements in Diffusion Transformers (DiTs) have established them as
the state-of-the-art method for video generation. However, their inherently
sequential denoising process results in inevitable latency, limiting real-world
applicability. Existing acceleration methods either compromise visual quality
due to architectural modifications or fail to reuse intermediate features at
proper granularity. Our analysis reveals that DiT blocks are the primary
contributors to inference latency. Across diffusion timesteps, the feature
variations of DiT blocks exhibit a U-shaped pattern with high similarity during
intermediate timesteps, which suggests substantial computational redundancy. In
this paper, we propose Block-Wise Caching (BWCache), a training-free method to
accelerate DiT-based video generation. BWCache dynamically caches and reuses
features from DiT blocks across diffusion timesteps. Furthermore, we introduce
a similarity indicator that triggers feature reuse only when the differences
between block features at adjacent timesteps fall below a threshold, thereby
minimizing redundant computations while maintaining visual fidelity. Extensive
experiments on several video diffusion models demonstrate that BWCache achieves
up to 2.24$\times$ speedup with comparable visual quality.

## 🔍 Abstract (한글 번역)

최근 확산 변환기(Diffusion Transformers, DiTs)의 발전은 이를 비디오 생성의 최첨단 방법으로 자리매김하게 했습니다. 그러나, 이들의 본질적으로 순차적인 노이즈 제거 과정은 불가피한 지연을 초래하여 실제 적용 가능성을 제한합니다. 기존의 가속화 방법은 구조적 수정으로 인해 시각적 품질을 저하시키거나 적절한 세분성에서 중간 특징을 재사용하지 못합니다. 우리의 분석에 따르면, DiT 블록이 추론 지연의 주요 원인임을 알 수 있습니다. 확산 시간 단계 전반에 걸쳐, DiT 블록의 특징 변이는 중간 시간 단계에서 높은 유사성을 보이며 U자형 패턴을 나타내어 상당한 계산 중복성을 시사합니다. 본 논문에서는 DiT 기반 비디오 생성을 가속화하기 위한 훈련이 필요 없는 방법인 블록 단위 캐싱(Block-Wise Caching, BWCache)을 제안합니다. BWCache는 확산 시간 단계 전반에 걸쳐 DiT 블록의 특징을 동적으로 캐싱하고 재사용합니다. 또한, 인접한 시간 단계에서 블록 특징 간의 차이가 특정 임계값 이하일 때만 특징 재사용을 유발하는 유사성 지표를 도입하여, 시각적 충실도를 유지하면서 불필요한 계산을 최소화합니다. 여러 비디오 확산 모델에 대한 광범위한 실험을 통해 BWCache가 비슷한 시각적 품질을 유지하면서 최대 2.24배의 속도 향상을 달성함을 입증합니다.

## 📝 요약

이 논문은 비디오 생성 분야에서 최첨단 기법으로 자리 잡은 Diffusion Transformers(DiTs)의 속도를 향상시키기 위한 방법을 제안합니다. DiTs는 순차적인 노이즈 제거 과정으로 인해 지연이 발생해 실용성이 제한되는데, 기존 가속화 방법은 시각적 품질을 저하시키거나 중간 특징을 적절히 재사용하지 못합니다. 저자들은 DiT 블록이 추론 지연의 주요 원인임을 밝혀냈으며, 중간 단계에서 특징의 유사성이 높아 계산 중복이 크다는 점을 발견했습니다. 이를 해결하기 위해, DiT 기반 비디오 생성의 속도를 높이는 BWCache라는 훈련이 필요 없는 방법을 제안합니다. BWCache는 DiT 블록의 특징을 동적으로 캐싱하고 재사용하며, 유사성 지표를 도입해 특징 재사용을 최적화합니다. 실험 결과, BWCache는 시각적 품질을 유지하면서 최대 2.24배의 속도 향상을 달성했습니다.

## 🎯 주요 포인트

- 1. Diffusion Transformers(DiTs)는 비디오 생성에서 최첨단 방법으로 자리 잡았지만, 순차적 디노이징 과정으로 인해 지연이 발생하여 실용성이 제한됩니다.

- 2. DiT 블록은 추론 지연의 주요 원인으로, 중간 타임스텝에서 특징 변화가 높은 유사성을 보여 계산 중복이 큽니다.

- 3. Block-Wise Caching(BWCache)는 DiT 기반 비디오 생성의 속도를 높이기 위한 훈련이 필요 없는 방법으로, 타임스텝 간 DiT 블록의 특징을 동적으로 캐시하고 재사용합니다.

- 4. 유사성 지표를 도입하여 인접 타임스텝의 블록 특징 차이가 일정 임계값 이하일 때만 특징 재사용을 유도하여 시각적 품질을 유지하면서 중복 계산을 최소화합니다.

- 5. 여러 비디오 확산 모델에 대한 실험 결과, BWCache는 시각적 품질을 유지하면서 최대 2.24배의 속도 향상을 달성했습니다.

---

*Generated on 2025-09-20 09:32:48*