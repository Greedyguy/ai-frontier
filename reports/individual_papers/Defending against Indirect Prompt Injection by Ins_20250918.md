
# Defending against Indirect Prompt Injection by Instruction Detection

**Korean Title:** 명령 감지를 통한 간접 프롬프트 주입에 대한 방어

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Instruction Detection|Instruction Detection]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Retrieval-Augmented Generation|Retrieval-Augmented Generation]] [[keywords/specific/InstructDetector|InstructDetector]] [[keywords/unique/BIPIA|BIPIA]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Instruction Detection
**🔬 Broad Technical**: Large Language Models, Retrieval-Augmented Generation
**🔗 Specific Connectable**: InstructDetector
**⭐ Unique Technical**: IPI attacks

**ArXiv ID**: [2505.06311](https://arxiv.org/abs/2505.06311)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2505.06311.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Retrieval-Augmented Generation` • 

`Instruction Detection` • 

`InstructDetector` • 

`Indirect Prompt Injection`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.06311v2 Announce Type: replace-cross 
Abstract: The integration of Large Language Models (LLMs) with external sources is becoming increasingly common, with Retrieval-Augmented Generation (RAG) being a prominent example. However, this integration introduces vulnerabilities of Indirect Prompt Injection (IPI) attacks, where hidden instructions embedded in external data can manipulate LLMs into executing unintended or harmful actions. We recognize that IPI attacks fundamentally rely on the presence of instructions embedded within external content, which can alter the behavioral states of LLMs. Can the effective detection of such state changes help us defend against IPI attacks? In this paper, we propose InstructDetector, a novel detection-based approach that leverages the behavioral states of LLMs to identify potential IPI attacks. Specifically, we demonstrate the hidden states and gradients from intermediate layers provide highly discriminative features for instruction detection. By effectively combining these features, InstructDetector achieves a detection accuracy of 99.60% in the in-domain setting and 96.90% in the out-of-domain setting, and reduces the attack success rate to just 0.03% on the BIPIA benchmark. The code is publicly available at https://github.com/MYVAE/Instruction-detection.

## 🔍 Abstract (한글 번역)

arXiv:2505.06311v2 발표 유형: replace-cross
요약: 대규모 언어 모델 (LLMs)과 외부 소스의 통합은 점점 더 흔해지고 있으며, 검색 증강 생성 (RAG)이 그 중 한 예입니다. 그러나 이 통합은 간접 프롬프트 주입 (IPI) 공격의 취약점을 소개하며, 여기서 외부 데이터에 잠재된 숨겨진 명령문이 LLMs가 의도하지 않은 또는 해로운 작업을 실행하도록 조작할 수 있습니다. 우리는 IPI 공격이 기본적으로 외부 콘텐츠에 내장된 명령문의 존재에 의존한다는 것을 인식하며, 이는 LLMs의 행동 상태를 변경할 수 있습니다. 이러한 상태 변경을 효과적으로 감지함으로써 우리는 IPI 공격에 대항할 수 있을까요? 본 논문에서는 잠재적인 IPI 공격을 식별하기 위해 LLMs의 행동 상태를 활용하는 InstructDetector라는 새로운 감지 기반 접근 방법을 제안합니다. 구체적으로, 중간 레이어의 숨겨진 상태와 그래디언트가 명령문 감지를 위한 매우 식별력 있는 특징을 제공한다는 것을 보여줍니다. 이러한 특징을 효과적으로 결합함으로써 InstructDetector는 도메인 내 설정에서 99.60%의 감지 정확도와 도메인 외 설정에서 96.90%의 감지 정확도를 달성하며, BIPIA 벤치마크에서 공격 성공률을 0.03%로 줄입니다. 코드는 https://github.com/MYVAE/Instruction-detection에서 공개적으로 이용 가능합니다.

## 📝 요약

이 연구는 대규모 언어 모델과 외부 소스의 통합이 점점 더 일반적으로 이루어지는 가운데, 외부 데이터에 숨겨진 지시 사항이 언어 모델을 조작하여 의도하지 않은 행동을 유발하는 간접 프롬프트 주입 (IPI) 공격의 취약점을 인식하고자 한다. 이 논문에서는 InstructDetector라는 새로운 감지 기반 접근 방식을 제안하며, 중간층의 숨겨진 상태와 그래디언트가 지시 감지에 매우 식별력 있는 특징을 제공한다는 것을 보여준다. 이를 효과적으로 결합함으로써 InstructDetector는 도메인 내 설정에서 99.60%의 감지 정확도와 도메인 외 설정에서 96.90%의 감지 정확도를 달성하며, BIPIA 벤치마크에서 공격 성공률을 0.03%로 낮춘다.

## 🎯 주요 포인트


- 대형 언어 모델과 외부 소스의 통합은 증가하고 있으며, 이로 인해 간접 프롬프트 주입 공격에 취약성이 증가하고 있다.

- 새로운 감지 기반 접근 방식 InstructDetector를 제안하여, LLM의 행동 상태를 활용하여 잠재적인 IPI 공격을 식별한다.

- 중간 레이어의 숨겨진 상태와 그래디언트는 명령 감지를 위한 매우 식별력 있는 특징을 제공하며, InstructDetector는 높은 정확도로 IPI 공격을 탐지할 수 있다.


---

*Generated on 2025-09-18 16:33:15*