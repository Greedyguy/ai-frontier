# LongCat-Flash Technical Report

**Korean Title:** 롱캣-플래시 기술 보고서

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Shortcut Connected MoE

## 🔗 유사한 논문
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (80.8% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (80.8% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (79.8% similar)
- [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (79.8% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01322v2 Announce Type: replace-cross 
Abstract: We introduce LongCat-Flash, a 560-billion-parameter Mixture-of-Experts (MoE) language model designed for both computational efficiency and advanced agentic capabilities. Stemming from the need for scalable efficiency, LongCat-Flash adopts two novel designs: (a) Zero-computation Experts, which enables dynamic computational budget allocation and activates 18.6B-31.3B (27B on average) per token depending on contextual demands, optimizing resource usage. (b) Shortcut-connected MoE, which enlarges the computation-communication overlap window, demonstrating notable gains in inference efficiency and throughput compared to models of a comparable scale. We develop a comprehensive scaling framework for large models that combines hyperparameter transfer, model-growth initialization, a multi-pronged stability suite, and deterministic computation to achieve stable and reproducible training. Notably, leveraging the synergy among scalable architectural design and infrastructure efforts, we complete model training on more than 20 trillion tokens within 30 days, while achieving over 100 tokens per second (TPS) for inference at a cost of \$0.70 per million output tokens. To cultivate LongCat-Flash towards agentic intelligence, we conduct a large-scale pre-training on optimized mixtures, followed by targeted mid- and post-training on reasoning, code, and instructions, with further augmentation from synthetic data and tool use tasks. Comprehensive evaluations demonstrate that, as a non-thinking foundation model, LongCat-Flash delivers highly competitive performance among other leading models, with exceptional strengths in agentic tasks. The model checkpoint of LongCat-Flash is open-sourced to foster community research.
  LongCat Chat: https://longcat.ai
  Hugging Face: https://huggingface.co/meituan-longcat
  GitHub: https://github.com/meituan-longcat

## 🔍 Abstract (한글 번역)

arXiv:2509.01322v2 발표 유형: 교차 교체  
초록: 우리는 계산 효율성과 고급 에이전트 기능을 동시에 고려하여 설계된 5600억 매개변수의 전문가 혼합(Mixture-of-Experts, MoE) 언어 모델인 LongCat-Flash를 소개합니다. 확장 가능한 효율성에 대한 필요성에서 출발하여, LongCat-Flash는 두 가지 새로운 설계를 채택했습니다: (a) 제로 계산 전문가(Zero-computation Experts)는 동적 계산 예산 할당을 가능하게 하며, 문맥적 요구에 따라 토큰당 평균 27B(18.6B-31.3B)를 활성화하여 자원 사용을 최적화합니다. (b) 단축 연결 MoE(Shortcut-connected MoE)는 계산-통신 중첩 창을 확장하여, 유사한 규모의 모델과 비교했을 때 추론 효율성과 처리량에서 주목할 만한 향상을 보여줍니다. 우리는 하이퍼파라미터 전이, 모델 성장 초기화, 다각적 안정성 스위트, 결정론적 계산을 결합하여 안정적이고 재현 가능한 훈련을 달성하는 대규모 모델을 위한 포괄적인 확장 프레임워크를 개발했습니다. 특히, 확장 가능한 아키텍처 설계와 인프라 노력 간의 시너지를 활용하여, 30일 이내에 20조 이상의 토큰에 대한 모델 훈련을 완료했으며, 백만 출력 토큰당 \$0.70의 비용으로 초당 100개 이상의 토큰(TPS)을 추론할 수 있었습니다. LongCat-Flash를 에이전트 지능으로 발전시키기 위해, 최적화된 혼합물에 대한 대규모 사전 훈련을 수행한 후, 추론, 코드 및 지침에 대한 중간 및 후속 훈련을 목표로 하였으며, 합성 데이터 및 도구 사용 작업을 통해 추가 보강을 진행했습니다. 종합적인 평가 결과, LongCat-Flash는 비사고 기반 모델로서 다른 선도적인 모델들 사이에서 매우 경쟁력 있는 성능을 제공하며, 특히 에이전트 작업에서 뛰어난 강점을 보입니다. LongCat-Flash의 모델 체크포인트는 커뮤니티 연구를 촉진하기 위해 오픈 소스로 제공됩니다.
  LongCat Chat: https://longcat.ai
  Hugging Face: https://huggingface.co/meituan-longcat
  GitHub: https://github.com/meituan-longcat

## 📝 요약

LongCat-Flash는 5600억 개의 매개변수를 가진 혼합 전문가(MoE) 언어 모델로, 효율성과 에이전트 기능을 동시에 추구합니다. 이 모델은 두 가지 혁신적인 설계를 도입했습니다. 첫째, '제로 컴퓨테이션 전문가'는 문맥에 따라 동적으로 계산 자원을 할당하여 평균 270억 개의 매개변수를 활성화함으로써 자원 사용을 최적화합니다. 둘째, '지름길 연결 MoE'는 계산-통신 중첩을 확대하여 유사 규모 모델 대비 추론 효율성을 향상시킵니다. 이 모델은 30일 내에 20조 개 이상의 토큰으로 훈련을 완료했으며, 초당 100개 이상의 토큰 추론 속도를 달성했습니다. 또한, 에이전트 지능을 위해 대규모 사전 훈련과 추가 훈련을 통해 뛰어난 성능을 보이며, 체크포인트는 오픈 소스로 제공됩니다.

## 🎯 주요 포인트

- 1. LongCat-Flash는 5600억 개의 매개변수를 가진 Mixture-of-Experts(MoE) 언어 모델로, 계산 효율성과 고급 에이전트 기능을 위해 설계되었습니다.

- 2. Zero-computation Experts와 Shortcut-connected MoE라는 두 가지 혁신적인 설계를 채택하여 문맥적 요구에 따라 동적으로 계산 자원을 최적화하고, 추론 효율성과 처리량을 향상시켰습니다.

- 3. 대규모 모델의 안정적이고 재현 가능한 훈련을 위해 하이퍼파라미터 전이, 모델 성장 초기화, 다각적 안정성 스위트, 결정론적 계산을 결합한 포괄적인 스케일링 프레임워크를 개발했습니다.

- 4. LongCat-Flash는 30일 내에 20조 개 이상의 토큰으로 모델 훈련을 완료하며, 추론 시 초당 100개 이상의 토큰을 처리하고 백만 개 출력 토큰당 \$0.70의 비용을 달성했습니다.

- 5. LongCat-Flash는 에이전트 지능을 위해 대규모 사전 훈련과 목표 지향적 중간 및 후속 훈련을 수행했으며, 모델 체크포인트는 커뮤니티 연구를 위해 오픈 소스로 제공됩니다.

---

*Generated on 2025-09-22 15:00:44*