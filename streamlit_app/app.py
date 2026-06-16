# Adobe Stock Search Volume Tool

import streamlit as st
import pandas as pd
import time

from fetch_utils import fetch_count, parse_events, build_xlsx

st.set_page_config(
    page_title="Adobe Stock Search Volume Tool",
    page_icon="📊",
    layout="centered",
)

st.title("📊 Adobe Stock Search Volume Tool")
st.markdown(
    "Get live Adobe Stock Video search counts for any event or keyword. "
    "Paste your events below and we'll fetch the search volume for each one."
)

# ── Step 1: API Key ──
with st.expander("🔑 Jina AI API Key", expanded=True):
    st.markdown(
        "You need a **free Jina AI API key** to fetch search counts. "
        "[Get one here](https://jina.ai/api-dashboard) (1 minute, free)."
    )
    api_key = st.text_input(
        "Paste your Jina AI API key",
        type="password",
        placeholder="jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        help="Your key is used only for this session and is never stored.",
    )

# ── Step 2: Input Events ──
st.markdown("---")
st.subheader("📝 Enter Events")
st.markdown(
    "Paste one event per line. Optionally prefix with a date (e.g. "
    "`January 1 - New Year's Day`).\n\n"
    "**Examples:**\n"
    "```\nNew Year's Day\nValentine's Day\n"
    "January 1 - New Year's Day\n"
    "March 17 - St. Patrick's Day\n```"
)

pasted_text = st.text_area(
    "Events (one per line)",
    height=200,
    placeholder="New Year's Day\nValentine's Day\nSt. Patrick's Day\nDiwali\nChristmas Day",
)

# ── Step 3: Fetch ──
col1, col2 = st.columns([1, 3])
with col1:
    fetch_clicked = st.button("🚀 Get Search Counts", type="primary", use_container_width=True)

status_placeholder = st.empty()
results_placeholder = st.empty()

if fetch_clicked:
    if not api_key:
        st.error("Please enter your Jina AI API key first.")
        st.stop()

    if not pasted_text.strip():
        st.error("Please paste at least one event.")
        st.stop()

    events = parse_events(pasted_text)
    terms = [ev["name"] for ev in events]

    status_placeholder.info(f"Fetching counts for {len(terms)} events... (may take a moment)")

    progress_bar = st.progress(0)
    term_map = {}

    for i, term in enumerate(terms):
        progress_text = f"[{i+1}/{len(terms)}] {term}"
        progress_bar.progress((i) / len(terms), text=progress_text)

        count = fetch_count(term, api_key, delay=2.5 if i > 0 else 0)
        term_map[term] = count

    progress_bar.progress(1.0, text="Done!")

    # Show results table
    results = []
    for ev in events:
        count = term_map.get(ev["name"])
        results.append({
            "Date": ev["date"],
            "Event Name": ev["name"],
            "Search Count": f"{int(count):,}" if count and count.isdigit() else ("❌ N/A" if count is None else count),
        })

    df = pd.DataFrame(results)
    results_placeholder.dataframe(df, use_container_width=True, hide_index=True)

    # Count stats
    valid = sum(1 for v in term_map.values() if v and v.replace(",", "").isdigit())
    status_placeholder.success(
        f"✅ Done! {valid}/{len(terms)} events have valid search counts."
    )

    # Download button
    xlsx_bytes = build_xlsx(events, term_map)
    st.download_button(
        label="📥 Download as XLSX",
        data=xlsx_bytes,
        file_name="adobe_stock_search_volumes.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
    )

    # Show which returned N/A
    na_events = [ev["name"] for ev in events if term_map.get(ev["name"]) is None]
    if na_events:
        with st.expander(f"⚠️ {len(na_events)} events returned no results"):
            for name in na_events:
                st.write(f"• {name}")

# ── Footer ──
st.markdown("---")
st.caption(
    "Powered by [Jina AI Reader](https://jina.ai/api-dashboard). "
    "Your API key is never stored — it's used only for the current session."
)
