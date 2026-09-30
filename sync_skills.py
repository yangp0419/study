#!/usr/bin/env python3
import os
import re
from pathlib import Path

START_MARKER = "<!-- SKILLS_SUMMARY_START -->"
END_MARKER = "<!-- SKILLS_SUMMARY_END -->"

def scan_skills(skills_dir: Path):
    skills = []
    if not skills_dir.exists():
        return skills

    for item in sorted(skills_dir.iterdir()):
        if item.is_dir():
            skill_name = item.name
            desc = ""
            skill_yaml = item / "SKILL.yaml"
            skill_md = item / "README.md"
            if skill_yaml.exists():
                text = skill_yaml.read_text(encoding="utf-8")
                m_name = re.search(r"^name:\s*(.+)$", text, re.M)
                m_desc = re.search(r"^description:\s*(.+)$", text, re.M)
                if m_name:
                    skill_name = m_name.group(1).strip()
                if m_desc:
                    desc = m_desc.group(1).strip()
            elif skill_md.exists():
                text = skill_md.read_text(encoding="utf-8")
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                if lines:
                    desc = lines[0].lstrip("#").strip()
            skills.append({"name": skill_name, "desc": desc, "path": f"skills/{item.name}"})
    return skills

def generate_markdown_summary(skills):
    if not skills:
        return "*(暂无注册的 Skills)*"
    lines = [
        "| Skill 名称 | 描述 | 本地路径 |",
        "| :--- | :--- | :--- |"
    ]
    for s in skills:
        name = s["name"]
        desc = s["desc"] or "无详细说明"
        path = s["path"]
        lines.append(f"| `{name}` | {desc} | `{path}` |")
    return "\n".join(lines)

def update_file_with_skills(target_file: Path, summary_md: str):
    if not target_file.exists():
        return False

    content = target_file.read_text(encoding="utf-8")
    block = f"{START_MARKER}\n{summary_md}\n{END_MARKER}"

    if START_MARKER in content and END_MARKER in content:
        pattern = re.compile(f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}", re.DOTALL)
        new_content = pattern.sub(block, content)
    else:
        new_content = content.rstrip() + f"\n\n### 共享 Skills 概览\n{block}\n"

    target_file.write_text(new_content, encoding="utf-8")
    return True

def main():
    root = Path(__file__).resolve().parent
    skills_dir = root / "skills"
    target_dirs = [root / ".agent", root / ".claude", root / ".codex"]
    skills = scan_skills(skills_dir)
    summary_md = generate_markdown_summary(skills)

    agents_file = root / "AGENTS.md"
    if agents_file.exists():
        update_file_with_skills(agents_file, summary_md)
        print(f"[OK] 已同步 Skills 简介至: {agents_file}")

    skills_index_file = skills_dir / "README.md"
    skills_index_file.write_text(f"# 共享 Skills 索引目录\n\n所有 Agent 均共享以下本地 Skills 能力：\n\n{summary_md}\n", encoding="utf-8")
    print(f"[OK] 已更新共享技能主索引: {skills_index_file}")

    for t_dir in target_dirs:
        if not t_dir.exists():
            continue
        for f in t_dir.glob("*.md"):
            update_file_with_skills(f, summary_md)
            print(f"[OK] 已同步 Skills 简介至: {f}")

if __name__ == "__main__":
    main()
