
# Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding

**Korean Title:** 다중 모달 대형 언어 모델(LLM)의 잠재력 발휘를 통한 제로샷 시공간 비디오 그라운딩

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temporal-Augmented Assembling

## 🔗 유사한 논문
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.4% similar)
- [[Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.5% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.4% similar)
- [[Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (82.4% similar)
- [[Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15178v1 Announce Type: new 
Abstract: Spatio-temporal video grounding (STVG) aims at localizing the spatio-temporal tube of a video, as specified by the input text query. In this paper, we utilize multimodal large language models (MLLMs) to explore a zero-shot solution in STVG. We reveal two key insights about MLLMs: (1) MLLMs tend to dynamically assign special tokens, referred to as \textit{grounding tokens}, for grounding the text query; and (2) MLLMs often suffer from suboptimal grounding due to the inability to fully integrate the cues in the text query (\textit{e.g.}, attributes, actions) for inference. Based on these insights, we propose a MLLM-based zero-shot framework for STVG, which includes novel decomposed spatio-temporal highlighting (DSTH) and temporal-augmented assembling (TAS) strategies to unleash the reasoning ability of MLLMs. The DSTH strategy first decouples the original query into attribute and action sub-queries for inquiring the existence of the target both spatially and temporally. It then uses a novel logit-guided re-attention (LRA) module to learn latent variables as spatial and temporal prompts, by regularizing token predictions for each sub-query. These prompts highlight attribute and action cues, respectively, directing the model's attention to reliable spatial and temporal related visual regions. In addition, as the spatial grounding by the attribute sub-query should be temporally consistent, we introduce the TAS strategy to assemble the predictions using the original video frames and the temporal-augmented frames as inputs to help improve temporal consistency. We evaluate our method on various MLLMs, and show that it outperforms SOTA methods on three common STVG benchmarks.
  The code will be available at https://github.com/zaiquanyang/LLaVA_Next_STVG.

## 🔍 Abstract (한글 번역)

arXiv:2509.15178v1 발표 유형: 신규  
초록: 시공간 비디오 그라운딩(STVG)은 입력 텍스트 쿼리에 의해 지정된 비디오의 시공간 튜브를 로컬라이징하는 것을 목표로 합니다. 이 논문에서는 다중 모달 대형 언어 모델(MLLMs)을 활용하여 STVG에서 제로샷 솔루션을 탐구합니다. 우리는 MLLMs에 대한 두 가지 주요 통찰을 제시합니다: (1) MLLMs는 텍스트 쿼리를 그라운딩하기 위해 \textit{그라운딩 토큰}이라고 불리는 특별한 토큰을 동적으로 할당하는 경향이 있으며; (2) MLLMs는 텍스트 쿼리의 단서를 완전히 통합하지 못해 (\textit{예:} 속성, 행동) 최적이 아닌 그라운딩을 경험하는 경우가 많습니다. 이러한 통찰을 바탕으로, 우리는 MLLMs 기반의 제로샷 STVG 프레임워크를 제안하며, 이는 MLLMs의 추론 능력을 발휘하기 위한 새로운 분해된 시공간 강조(DSTH) 및 시간 보강 조립(TAS) 전략을 포함합니다. DSTH 전략은 먼저 원래 쿼리를 속성과 행동 하위 쿼리로 분리하여 대상의 존재를 시공간적으로 묻습니다. 그런 다음 새로운 로짓 유도 재주의(LRA) 모듈을 사용하여 각 하위 쿼리에 대한 토큰 예측을 정규화함으로써 잠재 변수를 시공간 프롬프트로 학습합니다. 이러한 프롬프트는 각각 속성과 행동 단서를 강조하여 모델의 주의를 신뢰할 수 있는 시공간 관련 시각적 영역으로 유도합니다. 또한, 속성 하위 쿼리에 의한 공간적 그라운딩은 시간적으로 일관되어야 하므로, 우리는 원래 비디오 프레임과 시간 보강 프레임을 입력으로 사용하여 예측을 조립하는 TAS 전략을 도입하여 시간적 일관성을 향상시키는 데 도움을 줍니다. 우리는 다양한 MLLMs에서 우리의 방법을 평가하였으며, 세 가지 일반적인 STVG 벤치마크에서 SOTA 방법을 능가함을 보여줍니다.  
코드는 https://github.com/zaiquanyang/LLaVA_Next_STVG에서 제공될 예정입니다.

## 📝 요약

이 논문은 시공간 비디오 그라운딩(STVG) 문제를 다루며, 멀티모달 대형 언어 모델(MLLM)을 활용한 제로샷 접근법을 제안합니다. 주요 기여는 MLLM의 두 가지 통찰을 기반으로 한 새로운 프레임워크로, 첫째, MLLM은 텍스트 쿼리를 그라운딩하기 위해 동적으로 특별 토큰을 할당하고, 둘째, 텍스트 쿼리의 단서를 완전히 통합하지 못해 최적의 그라운딩을 달성하지 못한다는 점입니다. 이를 해결하기 위해, 속성과 행동 서브 쿼리로 원래 쿼리를 분해하여 시공간적 하이라이팅(DSTH)과 시간 보강 조립(TAS) 전략을 제안합니다. DSTH는 속성과 행동 단서를 강조하여 모델의 주의를 신뢰할 수 있는 시공간 관련 시각 영역으로 유도합니다. TAS는 시간적 일관성을 높이기 위해 원본 비디오 프레임과 시간 보강 프레임을 사용하여 예측을 조립합니다. 제안된 방법은 세 가지 STVG 벤치마크에서 최신 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 논문은 다중 모달 대형 언어 모델(MLLMs)을 활용하여 공간-시간 비디오 그라운딩(STVG)의 제로샷 솔루션을 탐구합니다.

- 2. MLLMs는 텍스트 쿼리를 그라운딩하기 위해 동적으로 특수 토큰을 할당하지만, 텍스트 쿼리의 단서를 완전히 통합하지 못해 최적의 그라운딩을 수행하지 못하는 경우가 많습니다.

- 3. 제안된 MLLM 기반 제로샷 프레임워크는 분해된 시공간 강조(DSTH)와 시간 보강 조립(TAS) 전략을 포함하여 MLLMs의 추론 능력을 극대화합니다.

- 4. DSTH 전략은 속성과 행동 하위 쿼리로 원래 쿼리를 분리하여 대상의 존재를 공간적 및 시간적으로 탐색하고, 새로운 로짓 유도 재주목(LRA) 모듈을 사용하여 잠재 변수를 학습합니다.

- 5. TAS 전략은 속성 하위 쿼리에 의한 공간적 그라운딩이 시간적으로 일관되도록 원본 비디오 프레임과 시간 보강 프레임을 입력으로 사용하여 예측을 조립합니다.

---

*Generated on 2025-09-19 16:10:40*