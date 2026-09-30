---
name: "vocab-learner"
description: "Record, analyze and expand English words. Invoke whenever user asks about an English word, vocabulary meaning, etymology, or requests adding words to vocabulary."
---

# 英语单词学习与沉淀技能 (Vocab Learner)

本技能负责处理用户的英语单词提问，并规范化沉淀到 `English/Vocabulary/` 目录中。

## 触发场景
- 用户询问某个具体英文单词的含义、用法、搭配、辨析（如 “xxx是什么单词”、“xxx怎么用”）。
- 用户要求记录/添加单词到词汇库。

## 执行流程

1. **结构化解析并输出解答**：
   - 单词原形、音标（IPA）、词性。
   - **构词拆解与重点标注**：**必须明确标注**该单词包含的**前缀（Prefix）**、**词根（Root）**与**后缀（Suffix）**，并详细说明各构词成分的字面含义及组合推导逻辑。
   - 核心释义与真题/典型例句。
   - 常见高频考点搭配（Collocations）。
   - 派生词与同源词扩展。

2. **双向自动归档沉淀到词库**（必须同时更新对应文件）：
   - **生词本归档**：
     - 在 `English/Vocabulary/Word_Bank/README.md` 中追加记录，必须明确记录单词、音标、词性、核心考点、构词拆解及记录时间。
   - **词根归档（Roots）**：
     - 若单词含有核心词根：
       - 若已有该词根目录（如 `English/Vocabulary/Roots/<root>/README.md`），将该单词及其构词精讲、考点搭配追加到该词根文档的单词列表中；
       - 若该词根尚无独立目录但具有衍生价值，可在 `English/Vocabulary/Roots/<root>/` 下新建对应词根解析文档，并同步登记至 `English/Vocabulary/Roots/README.md` 和 `English/Vocabulary/README.md`。
   - **词缀归档（Affixes）**：
     - 若单词含有前缀（如 `ad-`, `dis-`, `re-` 等）或后缀（如 `-ment`, `-able`, `-ive` 等）：
       - 检查 `English/Vocabulary/Affixes/Prefixes/README.md` 或 `English/Vocabulary/Affixes/Suffixes/README.md` 中对应的词缀条目；
       - 若对应词缀的示例词列表中尚未包含该单词，必须将其作为典型例词补充写入，注明词性和简要释义。

3. **格式与规范**：
   - 保持与 `English/Vocabulary/` 现有文档规范统一的 Markdown 表格与排版格式。
