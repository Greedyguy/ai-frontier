
# Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization

**Korean Title:** 엔트로피 강화 다중 턴 선호도 최적화를 통해 코딩 에이전트 구축하기

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[keywords/Large Language Models|Large Language Models]] [[keywords/Testtime Scaling|Testtime Scaling]] [[keywords/Preference Optimization|Preference Optimization]] [[keywords/Multiturn Reasoning|Multiturn Reasoning]] [[keywords/Tool Integration|Tool Integration]] [[keywords/Entropyenhanced Framework|Entropyenhanced Framework]] [[keywords/Stateoftheart Results|Stateoftheart Results]] [[keywords/Model Finetuning|Model Finetuning]] [[keywords/Model Verifier|Model Verifier]] [[categories/cs.AI|cs.AI]]

**ArXiv ID**: [2509.12434](https://arxiv.org/abs/2509.12434)
**Published**: 2025-09-17
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.12434.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Testtime Scaling` • 

`Preference Optimization` • 

`Multiturn Reasoning` • 

`Tool Integration` • 

`Policy Entropy` • 

`Finetuning` • 

`Verifier Model` • 

`Stateoftheart Results` • 

`Swebench`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12434v1 Announce Type: new 
Abstract: Software engineering presents complex, multi-step challenges for Large Language Models (LLMs), requiring reasoning over large codebases and coordinated tool use. The difficulty of these tasks is exemplified by benchmarks like SWE-bench, where current LLMs still struggle to resolve real-world issues.
  A promising approach to enhance performance is test-time scaling (TTS), but its gains are heavily dependent on the diversity of model outputs.
  While standard alignment methods such as Direct Preference Optimization (DPO) and Kahneman-Tversky Optimization (KTO) are effective at aligning model outputs with human preferences, this process can come at the cost of reduced diversity, limiting the effectiveness of TTS.
  Additionally, existing preference optimization algorithms are typically designed for single-turn tasks and do not fully address the complexities of multi-turn reasoning and tool integration required for interactive coding agents.
  To bridge this gap, we introduce \sys, an entropy-enhanced framework that adapts existing preference optimization algorithms to the multi-turn, tool-assisted setting.
  \sys augments the preference objective to explicitly preserve policy entropy and generalizes learning to optimize over multi-turn interactions rather than single-turn responses.
  We validate \sys by fine-tuning a diverse suite of models from different families and sizes (up to 106B parameters).
  To maximize performance gains from TTS, we further propose a hybrid best-trajectory selection scheme combining a learned verifier model with model free approaches.
  On the \swebench leaderboard, our approach establishes new state-of-the-art results among open-weight models. A 30B parameter model trained with \sys ranks 1st on \lite and 4th on \verified on the open-weight leaderboard, surpassed only by models with over 10x more parameters(\eg$>$350B).

## 🔍 Abstract (한글 번역)

arXiv:2509.12434v1 발표 유형: 새로운
요약: 소프트웨어 공학은 대규모 언어 모델 (LLMs)에 대한 복잡하고 다단계적인 도전 과제를 제시하며, 대규모 코드베이스 및 조정된 도구 사용에 대한 추론이 필요합니다. 이러한 작업의 어려움은 현재 LLMs가 여전히 실제 문제를 해결하는 데 어려움을 겪는 SWE-bench와 같은 벤치마크에 의해 잘 나타납니다.
성능을 향상시키는 유망한 접근 방식은 테스트 시간 스케일링 (TTS)이지만, 그 이득은 모델 출력의 다양성에 크게 의존합니다.
직접적인 선호도 최적화 (DPO) 및 칸만-트벌스키 최적화 (KTO)와 같은 표준 정렬 방법은 모델 출력을 인간의 선호도와 일치시키는 데 효과적이지만, 이 과정은 다양성 감소로 이어질 수 있어 TTS의 효과를 제한할 수 있습니다.
또한, 기존의 선호도 최적화 알고리즘은 일반적으로 단일 턴 작업을 위해 설계되어 있으며 상호작용 코딩 에이전트에 필요한 다중 턴 추론 및 도구 통합의 복잡성을 완전히 다루지 못합니다.
이 간극을 메우기 위해, 우리는 기존의 선호도 최적화 알고리즘을 다중 턴, 도구 지원 설정에 적응시키는 엔트로피 강화 프레임워크인 \sys를 소개합니다.
\sys는 정책 엔트로피를 명시적으로 보존하도록 선호도 목표를 보완하고, 단일 턴 응답이 아닌 다중 턴 상호작용을 최적화하기 위해 학습을 일반화합니다.
우리는 \sys를 사용하여 다양한 가족 및 크기의 모델을 세밀하게 조정하고 (최대 106B 매개변수), TTS에서의 성능 향상을 극대화하기 위해 학습된 확인자 모델과 모델 프리 접근법을 결합한 하이브리드 최상 궤적 선택 체계를 제안합니다.
\swebench 리더보드에서, 우리의 접근 방식은 오픈 가중치 모델 중에서 새로운 최첨단 결과를 확립합니다. \sys로 훈련된 30B 매개변수 모델은 오픈 가중치 리더보드에서 \lite에서 1위를 차지하며, \verified에서는 4위를 차지합니다. 이는 10배 이상의 매개변수를 가진 모델에만 뒤쳐지는 결과입니다(\eg$>$350B).

## 📝 요약

최근 소프트웨어 공학 분야에서는 대규모 언어 모델(LLMs)이 대규모 코드베이스를 다루고 도구를 조화롭게 사용하는 복잡한 다단계 도전 과제를 제시하고 있습니다. 이러한 작업의 어려움은 SWE-bench와 같은 벤치마크에서 현재 LLMs가 여전히 실제 문제를 해결하는 데 어려움을 겪는 것으로 나

## 🎯 주요 포인트


- 소프트웨어 공학은 대규모 언어 모델에게 복잡하고 다단계적인 도전 과제를 제시하며, 현재의 언어 모델들은 실제 세계 문제를 해결하는 데 여전히 어려움을 겪고 있다.

- 테스트 시간 스케일링(TTS)은 성능을 향상시키는 유망한 접근 방식이지만, 모델 출력의 다양성에 크게 의존한다.

- 기존의 선호도 최적화 알고리즘은 주로 단일 턴 작업을 위해 설계되어 있으


---

*Generated on 2025-09-18 11:09:58*