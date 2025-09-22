# VCBench: Benchmarking LLMs in Venture Capital

**Korean Title:** VCBench: 벤처 캐피탈에서 대형 언어 모델(LLM) 벤치마킹

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Rick Chen|Rick Chen]] [[authors/Joseph Ternasky|Joseph Ternasky]] [[authors/Afriyie Samuel Kwesi|Afriyie Samuel Kwesi]] [[authors/Ben Griffin|Ben Griffin]] [[authors/Aaron Ontoyin Yin|Aaron Ontoyin Yin]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Benchmarking

## 🔗 유사한 논문
- [[Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (82.7% similar)
- [[ScaleCUA_ Scaling Open-Source Computer Use Agents with Cross-Platform Data_20250919|ScaleCUA Scaling Open-Source Computer Use Agents with Cross-Platform Data]] (78.7% similar)
- [[Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (78.4% similar)
- [[AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (78.2% similar)
- [[MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (78.1% similar)

## 📋 저자 정보

**Authors:** Rick Chen, Joseph Ternasky, Afriyie Samuel Kwesi, Ben Griffin, Aaron Ontoyin Yin, Zakari Salifu, Kelvin Amoaba, Xianling Mu, Fuat Alican, Yigit Ihlamur

## 📄 Abstract (원문)

Benchmarks such as SWE-bench and ARC-AGI demonstrate how shared datasets
accelerate progress toward artificial general intelligence (AGI). We introduce
VCBench, the first benchmark for predicting founder success in venture capital
(VC), a domain where signals are sparse, outcomes are uncertain, and even top
investors perform modestly. At inception, the market index achieves a precision
of 1.9%. Y Combinator outperforms the index by a factor of 1.7x, while tier-1
firms are 2.9x better. VCBench provides 9,000 anonymized founder profiles,
standardized to preserve predictive features while resisting identity leakage,
with adversarial tests showing more than 90% reduction in re-identification
risk. We evaluate nine state-of-the-art large language models (LLMs).
DeepSeek-V3 delivers over six times the baseline precision, GPT-4o achieves the
highest F0.5, and most models surpass human benchmarks. Designed as a public
and evolving resource available at vcbench.com, VCBench establishes a
community-driven standard for reproducible and privacy-preserving evaluation of
AGI in early-stage venture forecasting.

## 🔍 Abstract (한글 번역)

벤치마크인 SWE-bench와 ARC-AGI는 공유 데이터셋이 인공지능 일반화(AGI)로의 발전을 가속화하는 방법을 보여줍니다. 우리는 벤처 캐피탈(VC)에서 창업자의 성공을 예측하는 최초의 벤치마크인 VCBench를 소개합니다. 이 분야는 신호가 희박하고 결과가 불확실하며, 심지어 최고 투자자들도 보통의 성과를 내는 곳입니다. 초기 단계에서 시장 지수는 1.9%의 정밀도를 달성합니다. Y Combinator는 지수를 1.7배 초과하며, 1급 회사들은 2.9배 더 우수합니다. VCBench는 예측 기능을 보존하면서도 신원 유출을 방지하기 위해 표준화된 9,000개의 익명화된 창업자 프로필을 제공합니다. 적대적 테스트는 재식별 위험을 90% 이상 감소시킵니다. 우리는 최첨단 대형 언어 모델(LLM) 9개를 평가했습니다. DeepSeek-V3는 기준 정밀도를 6배 이상 향상시키고, GPT-4o는 가장 높은 F0.5를 달성하며, 대부분의 모델이 인간 벤치마크를 초과합니다. vcbench.com에서 이용 가능한 공개적이고 진화하는 자원으로 설계된 VCBench는 초기 단계 벤처 예측에서 AGI의 재현 가능하고 프라이버시를 보장하는 평가를 위한 커뮤니티 주도의 표준을 확립합니다.

## 📝 요약

VCBench는 벤처 캐피털 분야에서 창업자의 성공을 예측하는 첫 번째 벤치마크로, 신호가 희박하고 결과가 불확실한 이 분야에서 AGI의 발전을 가속화합니다. 시장 지수의 정밀도는 1.9%이며, Y Combinator는 이를 1.7배, 1등급 기업은 2.9배 초과합니다. VCBench는 9,000개의 익명화된 창업자 프로필을 제공하며, 재식별 위험을 90% 이상 줄였습니다. 9개의 최신 대형 언어 모델을 평가한 결과, DeepSeek-V3는 기준 정밀도를 6배 이상 초과하고, GPT-4o는 가장 높은 F0.5를 기록했으며, 대부분의 모델이 인간 벤치마크를 능가했습니다. VCBench는 재현 가능하고 개인정보를 보호하는 초기 벤처 예측의 표준을 설정합니다.

## 🎯 주요 포인트

- 1. VCBench는 벤처 캐피탈에서 창업자 성공 예측을 위한 최초의 벤치마크로, 신호가 희박하고 결과가 불확실한 도메인에서 활용된다.

- 2. VCBench는 9,000개의 익명화된 창업자 프로필을 제공하며, 예측 기능을 유지하면서 신원 유출을 방지하는 표준화된 데이터를 포함한다.

- 3. DeepSeek-V3 모델은 기준 정밀도를 6배 이상 초과하며, GPT-4o는 가장 높은 F0.5 점수를 달성한다.

- 4. 대부분의 대형 언어 모델(LLM)은 인간의 벤치마크를 능가하는 성능을 보인다.

- 5. VCBench는 재현 가능하고 개인정보를 보호하는 초기 단계 벤처 예측 평가를 위한 커뮤니티 주도의 표준을 확립한다.

---

*Generated on 2025-09-20 05:56:24*