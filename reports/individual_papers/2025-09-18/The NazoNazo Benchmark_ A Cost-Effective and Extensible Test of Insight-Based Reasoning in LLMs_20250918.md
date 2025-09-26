---
keywords:
  - Large Language Models
  - Insight-Based Reasoning
  - Benchmark Saturation
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:05:12.475457",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Insight-Based Reasoning",
    "Benchmark Saturation"
  ],
  "rejected_keywords": [
    "Meta-Cognitive Weakness"
  ],
  "similarity_scores": {
    "Large Language Models": 0.85,
    "Insight-Based Reasoning": 0.7,
    "Benchmark Saturation": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# The NazoNazo Benchmark: A Cost-Effective and Extensible Test of Insight-Based Reasoning in LLMs

**Korean Title:** NazoNazo 벤치마크: 대규모 언어 모델(LLM)에서 통찰 기반 추론을 평가하기 위한 비용 효율적이고 확장 가능한 테스트

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Insight-Based Reasoning|Insight-Based Reasoning]], [[keywords/Benchmark Saturation|Benchmark Saturation]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (79.6% similar)
- [[Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models A Perspective from Schoenfeld's Episode Theory]] (78.7% similar)
- [[Humor in Pixels_ Benchmarking Large Multimodal Models Understanding of Online Comics_20250918|Humor in Pixels Benchmarking Large Multimodal Models Understanding of Online Comics]] (77.6% similar)
- [[Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (77.3% similar)
- [[Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (77.3% similar)

## 📋 저자 정보

**Authors:** Masaharu Mizumoto, Dat Nguyen, Zhiheng Han, Jiyuan Fang, Heyuan Guan, Xingfu Li, Naoya Shiraishi, Xuyang Tian, Yo Nakawake, Le Minh Nguyen

## 📄 Abstract (원문)

Benchmark saturation and contamination undermine confidence in LLM
evaluation. We present Nazonazo, a cost-effective and extensible benchmark
built from Japanese children's riddles to test insight-based reasoning. Items
are short (mostly one sentence), require no specialized domain knowledge, and
can be generated at scale, enabling rapid refresh of blind sets when leakage is
suspected. We evaluate 38 frontier models and 126 adults on 120 riddles. No
model except for GPT-5 is comparable to human performance, which achieves a
52.9% mean accuracy. Model comparison on extended 201 items shows that
reasoning models significantly outperform non-reasoning peers, while model size
shows no reliable association with accuracy. Beyond aggregate accuracy, an
informal candidate-tracking analysis of thought logs reveals many cases of
verification failure: models often produce the correct solution among
intermediate candidates yet fail to select it as the final answer, which we
illustrate with representative examples observed in multiple models. Nazonazo
thus offers a cost-effective, scalable, and easily renewable benchmark format
that addresses the current evaluation crisis while also suggesting a recurrent
meta-cognitive weakness, providing clear targets for future control and
calibration methods.

## 🔍 Abstract (한글 번역)

벤치마크 포화와 오염은 대규모 언어 모델(LLM) 평가에 대한 신뢰를 저해합니다. 우리는 통찰 기반의 추론을 테스트하기 위해 일본 어린이 수수께끼로 구성된 비용 효율적이고 확장 가능한 벤치마크인 Nazonazo를 제안합니다. 항목은 짧고(대부분 한 문장), 전문적인 도메인 지식을 필요로 하지 않으며, 대규모로 생성할 수 있어 유출이 의심될 때 블라인드 세트를 신속하게 갱신할 수 있습니다. 우리는 120개의 수수께끼에 대해 38개의 최첨단 모델과 126명의 성인을 평가했습니다. GPT-5를 제외한 어떤 모델도 인간의 성능과 비교할 수 없으며, 인간은 평균 52.9%의 정확도를 달성합니다. 확장된 201개 항목에 대한 모델 비교에서는 추론 모델이 비추론 모델보다 유의미하게 뛰어난 성능을 보였으며, 모델 크기와 정확도 간에는 신뢰할 만한 연관성이 없음을 보여줍니다. 집계된 정확도를 넘어, 사고 기록에 대한 비공식적인 후보 추적 분석은 많은 검증 실패 사례를 드러냅니다: 모델은 종종 중간 후보 중 올바른 해답을 생성하지만 이를 최종 답으로 선택하지 못하며, 이는 여러 모델에서 관찰된 대표적인 예로 설명됩니다. 따라서 Nazonazo는 현재의 평가 위기를 해결하면서도 반복적인 메타인지적 약점을 시사하며, 향후 제어 및 보정 방법을 위한 명확한 목표를 제공하는 비용 효율적이고 확장 가능하며 쉽게 갱신 가능한 벤치마크 형식을 제공합니다.

## 📝 요약

Nazonazo는 일본 어린이 수수께끼를 활용한 비용 효율적이고 확장 가능한 벤치마크로, 통찰 기반 추론을 평가합니다. 38개의 최신 모델과 126명의 성인을 대상으로 120개의 수수께끼를 평가한 결과, 인간의 평균 정확도는 52.9%로, GPT-5를 제외한 다른 모델들은 이에 미치지 못했습니다. 201개의 확장된 항목에서 추론 모델이 비추론 모델보다 성능이 뛰어났지만, 모델 크기와 정확도 간의 명확한 상관관계는 없었습니다. 생각의 기록을 분석한 결과, 모델들이 중간 후보 중 올바른 답을 생성하고도 최종 답으로 선택하지 못하는 경우가 많았습니다. Nazonazo는 현재 평가 위기를 해결하고, 모델의 메타인지적 약점을 드러내어 향후 개선의 목표를 제공합니다.

## 🎯 주요 포인트

- 1. Nazonazo는 일본 어린이 수수께끼를 활용하여 통찰 기반의 추론 능력을 평가하는 비용 효율적이고 확장 가능한 벤치마크입니다.

- 2. 38개의 최신 모델과 126명의 성인을 대상으로 한 평가에서 GPT-5를 제외한 모든 모델은 인간의 성능에 미치지 못했습니다.

- 3. 추론 모델은 비추론 모델보다 성능이 우수하며, 모델 크기와 정확도 간에는 신뢰할 만한 연관성이 없습니다.

- 4. 비공식적인 사고 추적 분석에서 모델이 중간 후보 중 올바른 해답을 제시하고도 최종 답으로 선택하지 못하는 검증 실패 사례가 다수 발견되었습니다.

- 5. Nazonazo는 현재의 평가 위기를 해결하고 미래의 제어 및 보정 방법을 위한 명확한 목표를 제공하는 벤치마크 형식을 제안합니다.

---

*Generated on 2025-09-20 05:45:12*