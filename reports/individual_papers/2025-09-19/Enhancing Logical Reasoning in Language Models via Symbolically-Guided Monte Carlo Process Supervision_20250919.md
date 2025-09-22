
# Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision

**Korean Title:** 언어 모델에서 논리적 추론을 강화하기 위한 상징적으로 유도된 몬테카를로 프로세스 감독

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Monte Carlo Estimation, Supervised Fine-Tuning

## 🔗 유사한 논문
- [[THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (85.4% similar)
- [[Explicit Reasoning Makes Better Judges A Systematic Study on Accuracy, Efficiency, and Robustness]] (85.2% similar)
- [[Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (85.1% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (85.0% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (84.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.20415v2 Announce Type: replace 
Abstract: Large language models (LLMs) have shown strong performance in many reasoning benchmarks. However, recent studies have pointed to memorization, rather than generalization, as one of the leading causes for such performance. LLMs, in fact, are susceptible to content variations, demonstrating a lack of robust planning or symbolic abstractions supporting their reasoning process. To improve reliability, many attempts have been made to combine LLMs with symbolic methods. Nevertheless, existing approaches fail to effectively leverage symbolic representations due to the challenges involved in developing reliable and scalable verification mechanisms. In this paper, we propose to overcome such limitations by synthesizing high-quality symbolic reasoning trajectories with stepwise pseudo-labels at scale via Monte Carlo estimation. A Process Reward Model (PRM) can be efficiently trained based on the synthesized data and then used to select more symbolic trajectories. The trajectories are then employed with Direct Preference Optimization (DPO) and Supervised Fine-Tuning (SFT) to improve logical reasoning and generalization. Our results on benchmarks (i.e., FOLIO and LogicAsker) show the effectiveness of the proposed method with gains on frontier and open-weight models. Moreover, additional experiments on claim verification data reveal that fine-tuning on the generated symbolic reasoning trajectories enhances out-of-domain generalizability, suggesting the potential impact of the proposed method in enhancing planning and logical reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2505.20415v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)은 많은 추론 벤치마크에서 강력한 성능을 보여주었습니다. 그러나 최근 연구들은 이러한 성능의 주요 원인 중 하나로 일반화보다는 암기를 지적하고 있습니다. 실제로 LLM은 콘텐츠 변형에 취약하며, 그들의 추론 과정을 뒷받침하는 견고한 계획이나 상징적 추상화가 부족함을 보여줍니다. 신뢰성을 향상시키기 위해, 많은 시도가 LLM을 상징적 방법과 결합하려고 했습니다. 그럼에도 불구하고, 기존 접근법은 신뢰할 수 있고 확장 가능한 검증 메커니즘을 개발하는 데 관련된 어려움 때문에 상징적 표현을 효과적으로 활용하지 못합니다. 본 논문에서는 몬테카를로 추정을 통해 단계별 의사 라벨을 사용하여 대규모로 고품질의 상징적 추론 경로를 합성함으로써 이러한 제한을 극복할 것을 제안합니다. 프로세스 보상 모델(PRM)은 합성된 데이터를 기반으로 효율적으로 훈련될 수 있으며, 이후 더 많은 상징적 경로를 선택하는 데 사용됩니다. 그런 다음 이 경로들은 논리적 추론과 일반화를 향상시키기 위해 직접 선호 최적화(DPO)와 지도 학습(SFT)과 함께 사용됩니다. 벤치마크(즉, FOLIO 및 LogicAsker)에서의 우리의 결과는 프론티어 및 오픈 웨이트 모델에서의 이득과 함께 제안된 방법의 효과를 보여줍니다. 게다가, 주장 검증 데이터에 대한 추가 실험은 생성된 상징적 추론 경로에 대한 미세 조정이 도메인 외 일반화를 향상시킨다는 것을 보여주며, 제안된 방법이 계획 및 논리적 추론을 향상시키는 데 미치는 잠재적 영향을 시사합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 성능이 기억에 의존하는 경향이 있으며, 일반화 능력이 부족하다는 문제를 지적합니다. 이를 해결하기 위해 저자들은 몬테카를로 추정을 통해 단계별 가짜 레이블을 사용하여 고품질의 상징적 추론 경로를 대량으로 생성하는 방법을 제안합니다. 이 데이터로 훈련된 프로세스 보상 모델(PRM)은 더 나은 상징적 경로를 선택하는 데 사용됩니다. 이러한 경로는 직접 선호 최적화(DPO)와 지도 학습(SFT)과 결합되어 논리적 추론과 일반화를 향상시킵니다. 실험 결과, 제안된 방법이 FOLIO와 LogicAsker 벤치마크에서 성능을 향상시켰으며, 주장 검증 데이터에서의 추가 실험은 생성된 상징적 추론 경로로 미세 조정 시 도메인 외 일반화 능력이 개선됨을 보여줍니다. 이는 계획 및 논리적 추론 향상에 기여할 가능성을 시사합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 성능은 기억보다는 일반화 부족으로 인해 콘텐츠 변형에 취약하다.

- 2. 신뢰성을 높이기 위해 LLM과 상징적 방법을 결합하려는 시도가 있었으나, 기존 접근법은 검증 메커니즘의 한계로 인해 효과적이지 않다.

- 3. 본 논문은 몬테카를로 추정을 통해 고품질의 상징적 추론 경로를 대규모로 생성하여 이러한 한계를 극복하고자 한다.

- 4. 생성된 데이터를 기반으로 효율적으로 훈련된 프로세스 보상 모델(PRM)은 더 나은 상징적 경로 선택에 사용된다.

- 5. 제안된 방법은 논리적 추론과 일반화를 개선하며, 생성된 상징적 추론 경로로의 미세 조정이 도메인 외 일반화 가능성을 높인다.

---

*Generated on 2025-09-19 15:59:59*