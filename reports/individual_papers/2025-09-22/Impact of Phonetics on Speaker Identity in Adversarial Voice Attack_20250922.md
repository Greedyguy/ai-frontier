# Impact of Phonetics on Speaker Identity in Adversarial Voice Attack

**Korean Title:** 음성 공격에서 발화자의 정체성에 미치는 음성학의 영향

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Phonetic-aware Defenses

## 🔗 유사한 논문
- [[2025-09-18/Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation_20250918|Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation]] (80.7% similar)
- [[2025-09-18/Discrete optimal transport is a strong audio adversarial attack_20250918|Discrete optimal transport is a strong audio adversarial attack]] (79.4% similar)
- [[2025-09-19/Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (78.9% similar)
- [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (78.2% similar)
- [[2025-09-19/Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (77.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15437v1 Announce Type: cross 
Abstract: Adversarial perturbations in speech pose a serious threat to automatic speech recognition (ASR) and speaker verification by introducing subtle waveform modifications that remain imperceptible to humans but can significantly alter system outputs. While targeted attacks on end-to-end ASR models have been widely studied, the phonetic basis of these perturbations and their effect on speaker identity remain underexplored. In this work, we analyze adversarial audio at the phonetic level and show that perturbations exploit systematic confusions such as vowel centralization and consonant substitutions. These distortions not only mislead transcription but also degrade phonetic cues critical for speaker verification, leading to identity drift. Using DeepSpeech as our ASR target, we generate targeted adversarial examples and evaluate their impact on speaker embeddings across genuine and impostor samples. Results across 16 phonetically diverse target phrases demonstrate that adversarial audio induces both transcription errors and identity drift, highlighting the need for phonetic-aware defenses to ensure the robustness of ASR and speaker recognition systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.15437v1 발표 유형: 교차  
초록: 음성에서의 적대적 교란은 인간에게는 감지되지 않지만 시스템의 출력을 크게 변경할 수 있는 미세한 파형 변화를 도입함으로써 자동 음성 인식(ASR) 및 화자 검증에 심각한 위협을 가합니다. 종단 간 ASR 모델에 대한 표적 공격은 널리 연구되었지만, 이러한 교란의 음성학적 기초와 화자 정체성에 미치는 영향은 충분히 탐구되지 않았습니다. 본 연구에서는 음성학적 수준에서 적대적 오디오를 분석하고, 교란이 모음 중심화 및 자음 대체와 같은 체계적인 혼동을 활용한다는 것을 보여줍니다. 이러한 왜곡은 전사 오류를 유발할 뿐만 아니라 화자 검증에 중요한 음성학적 단서를 저하시켜 정체성 이동을 초래합니다. DeepSpeech를 ASR 대상으로 사용하여 표적 적대적 예제를 생성하고, 진본 및 사칭 샘플 전반에 걸쳐 화자 임베딩에 미치는 영향을 평가합니다. 16개의 음성학적으로 다양한 목표 문구에 대한 결과는 적대적 오디오가 전사 오류와 정체성 이동을 모두 유발한다는 것을 보여주며, ASR 및 화자 인식 시스템의 견고성을 보장하기 위해 음성학적 인식을 고려한 방어의 필요성을 강조합니다.

## 📝 요약

이 논문은 음성의 적대적 교란이 자동 음성 인식(ASR)과 화자 검증 시스템에 미치는 영향을 분석합니다. 연구는 음성의 음소적 수준에서 교란이 모음 중앙화와 자음 대체와 같은 체계적인 혼동을 유발함을 보여줍니다. 이러한 왜곡은 전사 오류를 초래할 뿐만 아니라 화자 검증에 중요한 음성 단서를 손상시켜 화자 정체성의 변화를 유발합니다. DeepSpeech 모델을 대상으로 한 실험에서 적대적 예제가 전사 오류와 정체성 변화를 유도함을 확인하였으며, 이는 ASR 및 화자 인식 시스템의 견고성을 확보하기 위해 음소 인식 방어가 필요함을 강조합니다.

## 🎯 주요 포인트

- 1. 음성의 적대적 교란은 인간에게는 감지되지 않지만 자동 음성 인식(ASR) 및 화자 검증 시스템의 출력을 크게 변경할 수 있습니다.

- 2. 이 연구는 적대적 오디오의 음성적 수준 분석을 통해 모음 중앙화 및 자음 대체와 같은 체계적인 혼동을 이용하는 것을 보여줍니다.

- 3. 이러한 왜곡은 필사 오류를 유발할 뿐만 아니라 화자 검증에 중요한 음성적 단서를 손상시켜 정체성 변화를 초래합니다.

- 4. DeepSpeech를 ASR 대상으로 하여 생성된 적대적 예제는 필사 오류와 정체성 변화를 유도하며, 이는 ASR 및 화자 인식 시스템의 강건성을 보장하기 위한 음성 인식 방어의 필요성을 강조합니다.

---

*Generated on 2025-09-22 13:56:12*