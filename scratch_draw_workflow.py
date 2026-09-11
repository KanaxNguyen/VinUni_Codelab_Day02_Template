import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cấu hình font chữ hỗ trợ tiếng Việt trên Windows
plt.rcParams['font.family'] = 'Segoe UI'

def draw_workflow():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=200)
    ax.set_facecolor("#0F172A")  # Dark sleek background
    fig.patch.set_facecolor("#0F172A")

    # Title Banner
    plt.title("CURRENT-STATE WORKFLOW: VINHOMES RESIDENT INCIDENT TRIAGE & DISPATCH", 
              fontsize=18, fontweight='bold', color='#38BDF8', pad=25)
    plt.suptitle("Vin Smart Future — AI Product Scoping (Day 2 Codelab)", 
                 fontsize=12, color='#94A3B8', y=0.92)

    # Box coordinates & details
    steps = [
        {
            "num": "BUOC 1",
            "title": "Tiep nhan phan anh\n(App / Hotline)",
            "actor": "Actor: Le tan BQL",
            "time": "Thoi gian: 2 phut",
            "io": "In: Ticket tho | Out: Log he thong",
            "color": "#1E293B",
            "border": "#64748B",
            "is_bottleneck": False,
            "is_handoff": False,
            "x": 0.5, "y": 4.5
        },
        {
            "num": "BUOC 2 [BOTTLENECK]",
            "title": "Doc hieu text/anh &\nPhan loai su co",
            "actor": "Actor: Truc ban BQL",
            "time": "Thoi gian: 5 phut",
            "io": "In: Text/anh cam xuc | Out: Nhom su co",
            "color": "#450A0A",
            "border": "#EF4444",
            "is_bottleneck": True,
            "is_handoff": False,
            "x": 3.6, "y": 4.5
        },
        {
            "num": "BUOC 3 [BOTTLENECK]",
            "title": "Tra cuu so tay BQL &\nPhan cap xu ly",
            "actor": "Actor: Truc ban BQL",
            "time": "Thoi gian: 4 phut",
            "io": "In: So tay BQL | Out: Team ID phu trach",
            "color": "#450A0A",
            "border": "#EF4444",
            "is_bottleneck": True,
            "is_handoff": False,
            "x": 6.7, "y": 4.5
        },
        {
            "num": "BUOC 4 [BOTTLENECK]",
            "title": "Soan thao van ban\nphan hoi cu dan",
            "actor": "Actor: Truc ban BQL",
            "time": "Thoi gian: 5 phut",
            "io": "In: Hen gio SLA | Out: Tin nhan lich thiep",
            "color": "#450A0A",
            "border": "#EF4444",
            "is_bottleneck": True,
            "is_handoff": False,
            "x": 9.8, "y": 4.5
        },
        {
            "num": "BUOC 5 [HANDOFF]",
            "title": "Dieu phoi ban giao\nDoi ngu thuc dia",
            "actor": "Truc ban -> MEP/An ninh",
            "time": "Thoi gian: 2 phut",
            "io": "In: Lenh giao viec | Out: Ky thuat nhan ca",
            "color": "#064E3B",
            "border": "#10B981",
            "is_bottleneck": False,
            "is_handoff": True,
            "x": 12.9, "y": 4.5
        }
    ]

    w, h = 2.6, 2.8

    # Draw steps
    for step in steps:
        # Card container
        rect = patches.FancyBboxPatch(
            (step["x"], step["y"]), w, h,
            boxstyle="round,pad=0.15,rounding_size=0.2",
            linewidth=2.5 if (step["is_bottleneck"] or step["is_handoff"]) else 1.5,
            edgecolor=step["border"],
            facecolor=step["color"]
        )
        ax.add_patch(rect)

        # Header Badge
        badge_bg = "#EF4444" if step["is_bottleneck"] else ("#10B981" if step["is_handoff"] else "#334155")
        badge = patches.FancyBboxPatch(
            (step["x"] + 0.15, step["y"] + h - 0.55), w - 0.3, 0.4,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            linewidth=0, facecolor=badge_bg
        )
        ax.add_patch(badge)
        ax.text(step["x"] + w/2, step["y"] + h - 0.35, step["num"],
                color="#FFFFFF", fontsize=9.5, fontweight='bold', ha='center', va='center')

        # Title
        ax.text(step["x"] + w/2, step["y"] + h - 1.05, step["title"],
                color="#F8FAFC", fontsize=10, fontweight='bold', ha='center', va='center')

        # Actor & Time
        ax.text(step["x"] + w/2, step["y"] + 0.95, step['actor'],
                color="#94A3B8", fontsize=8.5, ha='center', va='center')
        
        time_color = "#FCA5A5" if step["is_bottleneck"] else "#6EE7B7"
        ax.text(step["x"] + w/2, step["y"] + 0.65, step["time"],
                color=time_color, fontsize=10.5, fontweight='bold', ha='center', va='center')

        # I/O footer
        ax.text(step["x"] + w/2, step["y"] + 0.25, step["io"],
                color="#64748B", fontsize=7.5, style='italic', ha='center', va='center')

    # Draw Connecting Arrows
    for i in range(len(steps) - 1):
        x_start = steps[i]["x"] + w + 0.05
        x_end = steps[i+1]["x"] - 0.05
        y_arrow = 4.5 + h/2
        ax.annotate(
            "", xy=(x_end, y_arrow), xytext=(x_start, y_arrow),
            arrowprops=dict(arrowstyle="-|>", color="#38BDF8", lw=3.0, mutation_scale=18)
        )

    # Summary Panel (Bottom)
    summary_rect = patches.FancyBboxPatch(
        (0.5, 0.8), 15.0, 2.4,
        boxstyle="round,pad=0.2,rounding_size=0.2",
        linewidth=1.5, edgecolor="#334155", facecolor="#1E293B"
    )
    ax.add_patch(summary_rect)

    # Metrics Summary
    ax.text(1.0, 2.7, "[TONG QUAN HIEN TRANG VAN HANH THU CONG]", fontsize=11, fontweight='bold', color='#38BDF8')
    ax.text(1.0, 1.8, "- Tong thoi gian xu ly: 18 phut / luot phan anh\n- Thoi gian lang phi tai Bottlenecks (Buoc 2, 3, 4): 14 phut (77.8%)\n- So luong tiep nhan: 150 - 300 ticket / ngay / dai do thi", 
            fontsize=9.5, color='#E2E8F0', va='center', linespacing=1.6)

    # Legend
    ax.text(8.8, 2.7, "[CHU THICH KY HIEU STANDARDS]", fontsize=11, fontweight='bold', color='#38BDF8')
    ax.text(8.8, 1.8, "[DO] BOTTLENECK: Diem nghen ton thoi gian & xu ly ngon ngu cam xuc phuc tap.\n[XANH] HANDOFF: Diem chuyen giao thong tin giua Ban Quan Ly va Doi thuc dia.\n[MUC TIEU] AI Copilot: Giam thoi gian tu 18 phut -> duoi 2 phut (Tang toc 90%).",
            fontsize=9.5, color='#E2E8F0', va='center', linespacing=1.6)

    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    plt.tight_layout()
    output_path = "d:/VinUni/VinUni_Codelab_Day02_Template/04-workflow-diagram.png"
    plt.savefig(output_path, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none', dpi=200)
    print(f"Workflow diagram successfully saved to {output_path}")

if __name__ == "__main__":
    draw_workflow()

