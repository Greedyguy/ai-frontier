# SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models

**Korean Title:** SightSound-R1: 시각에서 오디오 언어 모델로의 교차 모달 추론 증류

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Audio-Visual Question Answering

## 🔗 유사한 논문
- [[2025-09-18/Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (85.5% similar)
- [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (84.2% similar)
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (83.7% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (83.0% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (81.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15661v1 Announce Type: cross 
Abstract: While large audio-language models (LALMs) have demonstrated state-of-the-art audio understanding, their reasoning capability in complex soundscapes still falls behind large vision-language models (LVLMs). Compared to the visual domain, one bottleneck is the lack of large-scale chain-of-thought audio data to teach LALM stepwise reasoning. To circumvent this data and modality gap, we present SightSound-R1, a cross-modal distillation framework that transfers advanced reasoning from a stronger LVLM teacher to a weaker LALM student on the same audio-visual question answering (AVQA) dataset. SightSound-R1 consists of three core steps: (i) test-time scaling to generate audio-focused chains of thought (CoT) from an LVLM teacher, (ii) audio-grounded validation to filter hallucinations, and (iii) a distillation pipeline with supervised fine-tuning (SFT) followed by Group Relative Policy Optimization (GRPO) for the LALM student. Results show that SightSound-R1 improves LALM reasoning performance both in the in-domain AVQA test set as well as in unseen auditory scenes and questions, outperforming both pretrained and label-only distilled baselines. Thus, we conclude that vision reasoning can be effectively transferred to audio models and scaled with abundant audio-visual data.

## 🔍 Abstract (한글 번역)

arXiv:2509.15661v1 발표 유형: 교차  
초록: 대형 오디오-언어 모델(LALMs)은 최첨단 오디오 이해를 보여주었지만, 복잡한 사운드스케이프에서의 추론 능력은 여전히 대형 비전-언어 모델(LVLMs)에 뒤처져 있습니다. 시각적 도메인과 비교할 때, 하나의 병목 현상은 LALM의 단계별 추론을 가르칠 대규모 연쇄 사고 오디오 데이터의 부족입니다. 이러한 데이터 및 모달리티 격차를 해소하기 위해, 우리는 SightSound-R1을 제시합니다. 이는 강력한 LVLM 교사로부터 약한 LALM 학생에게 동일한 오디오-비주얼 질문 응답(AVQA) 데이터셋에서 고급 추론을 전이하는 교차 모달 증류 프레임워크입니다. SightSound-R1은 세 가지 핵심 단계로 구성됩니다: (i) LVLM 교사로부터 오디오 중심의 사고 사슬(CoT)을 생성하기 위한 테스트 시간 확장, (ii) 환각을 걸러내기 위한 오디오 기반 검증, (iii) LALM 학생을 위한 감독 하에 미세 조정(SFT) 후 그룹 상대 정책 최적화(GRPO)를 포함하는 증류 파이프라인. 결과는 SightSound-R1이 사전 학습된 모델과 레이블만 증류된 기준선을 능가하여, 도메인 내 AVQA 테스트 세트뿐만 아니라 보지 못한 청각적 장면과 질문에서도 LALM의 추론 성능을 향상시킴을 보여줍니다. 따라서 우리는 비전 추론이 오디오 모델로 효과적으로 전이될 수 있으며, 풍부한 오디오-비주얼 데이터로 확장될 수 있음을 결론지었습니다.

## 📝 요약

이 논문은 대규모 오디오-언어 모델(LALM)의 복잡한 소리 환경에서의 추론 능력을 향상시키기 위해 SightSound-R1이라는 교차 모달 증류 프레임워크를 제안합니다. 이는 강력한 시각-언어 모델(LVLM)로부터 오디오-비주얼 질문 응답(AVQA) 데이터셋에서 추론 능력을 전이하는 방법입니다. SightSound-R1은 LVLM 교사로부터 오디오 중심의 사고 체인을 생성하고, 오디오 기반 검증을 통해 오류를 걸러내며, 지도 학습과 그룹 상대 정책 최적화를 통해 LALM 학생 모델을 개선합니다. 실험 결과, 이 방법은 LALM의 추론 성능을 향상시켜 새로운 오디오 장면과 질문에서도 우수한 성능을 보였습니다. 이는 시각적 추론이 오디오 모델로 효과적으로 전이될 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 대형 오디오-언어 모델(LALM)은 최첨단 오디오 이해를 보여주지만, 복잡한 소리 환경에서의 추론 능력은 여전히 대형 비전-언어 모델(LVLM)에 뒤처진다.

- 2. SightSound-R1은 강력한 LVLM 교사의 고급 추론 능력을 약한 LALM 학생에게 전이시키는 교차 모달 증류 프레임워크이다.

- 3. SightSound-R1은 LVLM 교사로부터 오디오 중심의 사고 사슬(CoT)을 생성하고, 오디오 기반 검증을 통해 환각을 필터링하며, 감독된 미세 조정(SFT)과 그룹 상대 정책 최적화(GRPO)를 포함한 증류 파이프라인으로 구성된다.

- 4. SightSound-R1은 사전 훈련된 모델과 레이블만을 사용한 증류 기반을 능가하며, LALM의 추론 성능을 향상시킨다.

- 5. 시각적 추론은 오디오 모델로 효과적으로 전이될 수 있으며, 풍부한 오디오-비주얼 데이터를 통해 확장될 수 있다.

---

*Generated on 2025-09-22 14:07:07*