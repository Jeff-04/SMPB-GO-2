import streamlit as st
import base64
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SPMB Ganesha Operation",  page_icon="📚",layout="wide")

if "nilai_rapot_smp" not in st.session_state:
    st.session_state["nilai_rapot_smp"] = 0

if "nilai_tka_smp" not in st.session_state:
    st.session_state["nilai_tka_smp"] = 0

if "nilai_prestasi_smp" not in st.session_state:
    st.session_state["nilai_prestasi_smp"] = 0


if "nilai_rapot_sma" not in st.session_state:
    st.session_state["nilai_rapot_sma"] = 0

if "nilai_tka_sma" not in st.session_state:
    st.session_state["nilai_tka_sma"] = 0

if "nilai_prestasi_sma" not in st.session_state:
    st.session_state["nilai_prestasi_sma"] = 0

if "nilai_organisasi_sma" not in st.session_state:
    st.session_state["nilai_organisasi_sma"] = 0

def hitung_nilai_akhir(nilai_rapor, nilai_tka, skor_prestasi):

    # Jika prestasi langsung diterima
    if isinstance(skor_prestasi, str):
        return skor_prestasi

    nilai_akhir = (
        (0.30 * nilai_rapor)
        + (0.40 * nilai_tka)
        + (0.30 * skor_prestasi)
    )

    return round(nilai_akhir, 2)

def hitung_nilai_akhir_sma(nilai_rapor, nilai_tka, skor_prestasi, skor_organisasi):

    # Jika prestasi langsung diterima
    if isinstance(skor_prestasi, str):
        return skor_prestasi

    nilai_akhir = (
        (0.50 * nilai_rapor)
        + (0.50 * nilai_tka)
        + (skor_prestasi)
        + (skor_organisasi)
    )

    return round(nilai_akhir, 2)


def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Transparansi konten */
        .block-container {{
            background: transparent;
            padding-top: 0rem;
            padding-left: 2rem;
            padding-right: 2rem;
            padding-bottom: 2rem;
            max-width: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.markdown("""
<style>
.block-container{
    padding-top: 0rem !important;
    padding-left: 3rem;
    padding-right: 3rem;
}

[data-testid="stHeader"]{
    display:none;
}

[data-testid="stToolbar"]{
    display:none;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* Semua teks umum */
html, body, [class*="css"]  {
    color: #000000 !important;
}

/* Judul */
h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

/* Text biasa */
p, span, label, div {
    color: #000000 !important;
}

/* Input */
input, textarea {
    color: #000000 !important;
}

/* Selectbox */
[data-baseweb="select"] {
    color: #000000 !important;
}

/* Radio button */
.stRadio label {
    color: #000000 !important;
}

/* Checkbox */
.stCheckbox label {
    color: #000000 !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    color: #000000 !important;
}

/* Sidebar */
[data-testid="stSidebar"] * {
    color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* SELECTBOX */
.stSelectbox > div > div {
    background-color: white !important;
    color: black !important;
}

/* INPUT DI DALAM SELECTBOX */
.stSelectbox input {
    color: black !important;
}

/* DROPDOWN POPUP */
ul {
    background-color: white !important;
}

/* ITEM DROPDOWN */
li {
    background-color: white !important;
    color: black !important;
}

/* HOVER ITEM */
li:hover {
    background-color: #FFE082 !important;
    color: black !important;
}

/* BASEWEB POPUP */
[data-baseweb="menu"] {
    background-color: white !important;
}

[data-baseweb="menu"] * {
    color: black !important;
}

[data-baseweb="popover"] {
    background-color: white !important;
}

[data-baseweb="popover"] * {
    color: black !important;
}

/* OPTION YANG DIPILIH */
[role="option"] {
    background-color: white !important;
    color: black !important;
}

[role="option"]:hover {
    background-color: #FFE082 !important;
    color: black !important;
}

/* ========================= */
/* NUMBER INPUT */
/* ========================= */

.stNumberInput input {
    background-color: white !important;
    color: black !important;
    border: 1px solid #D60000 !important;
}

/* Container Number Input */
[data-testid="stNumberInput"] {
    background-color: transparent !important;
}

/* Tombol + dan - */
[data-testid="stNumberInput"] button {
    background-color: white !important;
    color: black !important;
    border: 1px solid #D60000 !important;
}

/* Hover tombol + dan - */
[data-testid="stNumberInput"] button:hover {
    background-color: #FFE082 !important;
    color: black !important;
}

/* Placeholder */
.stNumberInput input::placeholder {
    color: #666666 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* BUTTON */
.stButton > button,
[data-testid="stFormSubmitButton"] > button {

    background-color: #D60000 !important;
    color: white !important;

    border: none !important;
    border-radius: 10px !important;

    font-weight: bold !important;

    transition: all 0.3s ease;
}

/* HOVER */
.stButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {

    background-color: #FFD700 !important;
    color: #000000 !important;

    border: none !important;
}

/* CLICK */
.stButton > button:active,
[data-testid="stFormSubmitButton"] > button:active {

    background-color: #B00000 !important;
    color: white !important;
}

/* FOCUS */
.stButton > button:focus,
[data-testid="stFormSubmitButton"] > button:focus {

    box-shadow: 0 0 0 2px rgba(214,0,0,0.3) !important;
}

</style>
""", unsafe_allow_html=True)

# Apply background
set_background("Image.png")
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("""
    <div style='text-align:center;'>
        <h1 style='color:#D60000; margin-bottom:0px;'>
            🎓 GO SPMB Prestasi
        </h1>
        <p style='font-size:22px; color:black; margin-top:5px;'>
            Sistem Prediksi Peluang Masuk Sekolah melalui Jalur Prestasi
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

mapel_sma = [
    "Bahasa Indonesia",
    "PABP",
    "Bahasa Inggris",
    "PKn",
    "IPS-Sosiologi",
    "Matematika",
    "IPS-Sejarah",
    "IPA-Fisika",
    "Penjaskes",
    "PKWU",
    "IPA-Kimia",
    "Bahasa Jawa",
    "IPA-Biologi",
    "IPS-Geografi",
    "Informatika",
    "IPS-Ekonomi"
]

wajib_tka_sma = [
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Matematika"
]

pilihan_tka_sma = [
    "Geografi",
    "Sosiologi",
    "Ekonomi",
    "Fisika",
    "Kimia",
    "Biologi",
    "Matematika TL",
    "Sejarah",
    "Antropologi",
    "Pancasila",
    "Bahasa Indonesia TL",
    "Bahasa Inggris TL",
    "Bahasa Arab",
    "Bahasa Prancis",
    "Bahasa Korea",
    "Bahasa Jepang",
    "Bahasa Mandarin",
    "Bahasa Jerman"
]


mapel_smp = [
    "Pendidikan Agama dan Budi Pekerti",
    "Pendidikan Pancasila",
    "Bahasa Indonesia",
    "Matematika",
    "IPA",
    "IPS",
    "Bahasa Inggris",
    "PJOK",
    "Informatika",
    "Seni Budaya / Prakarya",
    "Bahasa Jawa"
]

tka_smp = [
    "Bahasa Indonesia",
    "Matematika",
]

col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    selected = option_menu(
        menu_title=None,
        options=["SMP", "SMA"],
        icons=["mortarboard", "mortarboard"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if selected=="SMP":
        nilai_rapor_mapel = {}
        with st.expander("Nilai Raport"):
            st.markdown("<h3 align='center'> Input Nilai Raport Siswa </h3", unsafe_allow_html=True)
            # Form Login
            with st.form("form_login"):
                for mapel in mapel_smp:
                    nilai_rapor_mapel[mapel] = st.number_input(
                        f"Nilai {mapel}",
                        min_value=0.0,
                        max_value=100.0,
                        step=0.1
                    )
                
                submit = st.form_submit_button("Submit", use_container_width=True)

                if submit:

                    st.success("Data berhasil disimpan!")

                    st.markdown("### 📊 Nilai yang Diinput")

                    total = 0

                    for mapel, nilai in nilai_rapor_mapel.items():
                        # st.write(f"**{mapel}** : {nilai}")
                        total += nilai

                    st.session_state["nilai_rapot_smp"] = total / len(nilai_rapor_mapel)

                    st.metric(
                        label="Rata-rata Nilai",
                        value=f"{total / len(nilai_rapor_mapel):.2f}"
                    )



        nilai_tka_mapel = {}
        with st.expander("Nilai TKA"):
            st.markdown("<h3 align='center'> Input Nilai TKA Siswa </h3", unsafe_allow_html=True)
            # Form Login
            with st.form("form_login_2"):
                for mapel in tka_smp:
                    nilai_tka_mapel[mapel] = st.number_input(
                        f"Nilai {mapel}",
                        min_value=0.0,
                        max_value=100.0,
                        step=0.1
                    )
                
                submit = st.form_submit_button("Submit", use_container_width=True)

                if submit:

                    st.success("Data berhasil disimpan!")

                    st.markdown("### 📊 Nilai yang Diinput")

                    total = 0

                    for mapel, nilai in nilai_tka_mapel.items():
                        # st.write(f"**{mapel}** : {nilai}")
                        total += nilai

                    st.session_state["nilai_tka_smp"] = total / len(nilai_tka_mapel)

                    st.metric(
                        label="Rata-rata Nilai",
                        value=f"{st.session_state["nilai_tka_smp"]:.2f}"
                    )

        with st.expander("🏆 Prestasi"):
            st.markdown(
                "<h3 align='center'> Input Data Prestasi Siswa </h3>",
                unsafe_allow_html=True
            )

            with st.form("form_prestasi"):

                kategori = st.selectbox(
                    "Kategori Prestasi",
                    [
                        "Perorangan",
                        "Kelompok"
                    ]
                )

                jenis_kejuaraan = st.selectbox(
                    "Jenis Kejuaraan",
                    [
                        "Berjenjang",
                        "Tidak Berjenjang"
                    ]
                )

                tingkat_kejuaraan = st.selectbox(
                    "Tingkat Kejuaraan",
                    [
                        "Internasional",
                        "Nasional",
                        "Provinsi",
                        "Karesidenan",
                        "Kabupaten"
                    ]
                )

                juara = st.selectbox(
                    "Peringkat",
                    [
                        "Juara I",
                        "Juara II",
                        "Juara III"
                    ]
                )

                submit_prestasi = st.form_submit_button(
                    "Submit",
                    use_container_width=True
                )

            if submit_prestasi:

                skor_prestasi = {

                    ("Perorangan", "Berjenjang"): {
                        "Karesidenan": {
                            "Juara I": 100,
                            "Juara II": 90,
                            "Juara III": 80
                        },
                        "Kabupaten": {
                            "Juara I": 70,
                            "Juara II": 60,
                            "Juara III": 50
                        }
                    },

                    ("Perorangan", "Tidak Berjenjang"): {
                        "Provinsi": {
                            "Juara I": 100,
                            "Juara II": 90,
                            "Juara III": 80
                        },
                        "Karesidenan": {
                            "Juara I": 70,
                            "Juara II": 60,
                            "Juara III": 50
                        },
                        "Kabupaten": {
                            "Juara I": 40,
                            "Juara II": 30,
                            "Juara III": 20
                        }
                    },

                    ("Kelompok", "Berjenjang"): {
                        "Karesidenan": {
                            "Juara I": 70,
                            "Juara II": 60,
                            "Juara III": 50
                        },
                        "Kabupaten": {
                            "Juara I": 40,
                            "Juara II": 30,
                            "Juara III": 20
                        }
                    },

                    ("Kelompok", "Tidak Berjenjang"): {
                        "Provinsi": {
                            "Juara I": 90,
                            "Juara II": 80,
                            "Juara III": 70
                        },
                        "Karesidenan": {
                            "Juara I": 60,
                            "Juara II": 50,
                            "Juara III": 40
                        },
                        "Kabupaten": {
                            "Juara I": 30,
                            "Juara II": 20,
                            "Juara III": 10
                        }
                    }
                }

                skor = None

                if kategori == "Perorangan" and jenis_kejuaraan == "Berjenjang":
                    if tingkat_kejuaraan in [
                        "Internasional",
                        "Nasional",
                        "Provinsi"
                    ]:
                        skor = "Langsung Diterima"

                elif kategori == "Kelompok" and jenis_kejuaraan == "Berjenjang":
                    if tingkat_kejuaraan in [
                        "Internasional",
                        "Nasional",
                        "Provinsi"
                    ]:
                        skor = "Langsung Diterima"

                elif tingkat_kejuaraan in [
                    "Internasional",
                    "Nasional"
                ]:
                    skor = "Langsung Diterima"

                if skor is None:
                    try:
                        skor = skor_prestasi[
                            (kategori, jenis_kejuaraan)
                        ][tingkat_kejuaraan][juara]
                    except:
                        skor = 0

                st.success("Data berhasil disimpan!")

                st.markdown("### 📊 Hasil Penilaian Prestasi")

                col_a, col_b = st.columns(2)

                with col_a:
                    st.write("**Kategori**")
                    st.write(kategori)

                    st.write("**Jenis Kejuaraan**")
                    st.write(jenis_kejuaraan)

                with col_b:
                    st.write("**Tingkat**")
                    st.write(tingkat_kejuaraan)

                    st.write("**Peringkat**")
                    st.write(juara)

                st.divider()
                st.session_state["nilai_prestasi_smp"] = skor
                if skor == "Langsung Diterima":
                    st.success("🎉 Status : Langsung Diterima")
                else:
                    st.metric(
                        "Skor Prestasi",
                        skor
                    )
        st.divider()

        nr = st.session_state.get("nilai_rapot_smp")
        tka = st.session_state.get("nilai_tka_smp")
        sp = st.session_state.get("nilai_prestasi_smp")
        print(nr,tka,sp)

        st.markdown("""
            <h2 style='text-align:center;color:#D60000'>
            📊 HASIL AKHIR PERHITUNGAN
            </h2>
        """, unsafe_allow_html=True)

        st.latex(
            r"NA = (0.30 \times NR) + (0.40 \times TKA) + (0.30 \times SP)"
        )

        if nr is not None and tka is not None and sp is not None:

            if sp == "Langsung Diterima":

                st.success(
                    "🎉 Siswa memenuhi kategori LANGSUNG DITERIMA berdasarkan prestasi."
                )

            else:

                nilai_akhir = hitung_nilai_akhir(
                    nr,
                    tka,
                    sp
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("📖 Nilai Rapor", f"{nr:.2f}")

                with col2:
                    st.metric("📝 Nilai TKA", f"{tka:.2f}")

                with col3:
                    st.metric("🏆 Skor Prestasi", f"{sp:.2f}")

                with col4:
                    st.metric("🎯 Nilai Akhir", f"{nilai_akhir:.2f}")
    

    elif selected=="SMA":
        nilai_rapor_mapel = {}
        with st.expander("Nilai Raport"):
            st.markdown("<h3 align='center'> Input Nilai Raport Siswa </h3", unsafe_allow_html=True)
            # Form Login
            with st.form("form_login"):
                for mapel in mapel_sma:
                    nilai_rapor_mapel[mapel] = st.number_input(
                        f"Nilai {mapel}",
                        min_value=0.0,
                        max_value=100.0,
                        step=0.1
                    )
                
                submit = st.form_submit_button("Submit", use_container_width=True)

                if submit:

                    st.success("Data berhasil disimpan!")

                    st.markdown("### 📊 Nilai yang Diinput")

                    total = 0

                    for mapel, nilai in nilai_rapor_mapel.items():
                        # st.write(f"**{mapel}** : {nilai}")
                        total += nilai

                    st.session_state["nilai_rapot_sma"] = total / len(nilai_rapor_mapel)

                    st.metric(
                        label="Rata-rata Nilai",
                        value=f"{total / len(nilai_rapor_mapel):.2f}"
                    )

        

        nilai_tka_mapel = {}
        with st.expander("Nilai TKA"):
            st.markdown("<h3 align='center'> Input Nilai TKA Siswa </h3", unsafe_allow_html=True)
            # Form Login
            with st.form("form_login_2"):
                for mapel in wajib_tka_sma:
                    nilai_tka_mapel[mapel] = st.number_input(
                        f"Nilai {mapel}",
                        min_value=0.0,
                        max_value=100.0,
                        step=0.1
                    )


                col1, col2 = st.columns(2)

                with col1:
                    pilihan_1 = st.selectbox(
                        "Mapel Pilihan 1",
                        options=pilihan_tka_sma,
                        index=None,
                        placeholder="Pilih mapel..."
                    )

                    nilai_1 = st.number_input(
                        "Nilai",
                        min_value=0.0,
                        max_value=100.0,
                        step=0.1,
                        key="nilai_1"
                    )

                    pilihan_2 = st.selectbox(
                        "Mapel Pilihan 2",
                        options=pilihan_tka_sma,
                        index=None,
                        placeholder="Pilih mapel..."
                    )

                    nilai_1 = st.number_input(
                        "Nilai",
                        min_value=0.0,
                        max_value=100.0,
                        step=0.1,
                        key="nilai_2"
                    )
                submit = st.form_submit_button("Submit", use_container_width=True)

                if submit:

                    st.success("Data berhasil disimpan!")

                    st.markdown("### 📊 Nilai yang Diinput")

                    total = 0

                    for mapel, nilai in nilai_tka_mapel.items():
                        # st.write(f"**{mapel}** : {nilai}")
                        total += nilai

                    st.session_state["nilai_tka_sma"] = total / len(nilai_tka_mapel)

                    st.metric(
                        label="Rata-rata Nilai",
                        value=f"{st.session_state["nilai_tka_sma"]:.2f}"
                    )

            
        
        with st.expander("🏆 Prestasi"):

            with st.form("form_prestasi_sma"):

                tingkat = st.selectbox(
                    "Tingkat Prestasi",
                    [
                        "Internasional",
                        "Nasional",
                        "Provinsi",
                        "Kab/Kota"
                    ]
                )

                juara = st.selectbox(
                    "Peringkat",
                    [
                        "Juara I",
                        "Juara II",
                        "Juara III"
                    ]
                )

                submit = st.form_submit_button(
                    "Simpan Prestasi",
                    use_container_width=True
                )

            if submit:

                skor_prestasi = {
                    "Internasional": {
                        "Juara I": "Langsung Diterima",
                        "Juara II": "Langsung Diterima",
                        "Juara III": "Langsung Diterima",
                    },
                    "Nasional": {
                        "Juara I": "Langsung Diterima",
                        "Juara II": 5.00,
                        "Juara III": 4.00,
                    },
                    "Provinsi": {
                        "Juara I": 3.00,
                        "Juara II": 2.75,
                        "Juara III": 2.50,
                    },
                    "Kab/Kota": {
                        "Juara I": 2.25,
                        "Juara II": 2.00,
                        "Juara III": 1.75,
                    }
                }

                skor = skor_prestasi[tingkat][juara]

                st.session_state["nilai_prestasi_sma"] = skor

                if skor == "Langsung Diterima":
                    st.success("🎉 Siswa Langsung Diterima")
                else:
                    st.metric(
                        "Bobot Prestasi",
                        f"+{skor:.2f}"
                    )

        with st.expander("👥 Organisasi"):

            st.markdown("""
            <h3 align='center'>Pengalaman Organisasi</h3>
            <p>Ketua OSIS / Ketua OSIM / Ketua MPK / Ketua BES / Ketua Pramuka</p>
            """, unsafe_allow_html=True)

            with st.form("form_organisasi"):

                organisasi = st.selectbox(
                    "Apakah siswa pernah menjabat sebagai salah satu berikut?",
                    [
                        "Tidak",
                        "Ya"
                    ]
                )

                submit_organisasi = st.form_submit_button(
                    "Simpan",
                    use_container_width=True
                )

            if submit_organisasi:

                if organisasi == "Ya":
                    st.session_state["nilai_organisasi_sma"] = 0.75
                else:
                    st.session_state["nilai_organisasi_sma"] = 0.0

                st.success("Data organisasi berhasil disimpan!")

                st.metric(
                    "Bobot Organisasi",
                    f"+{st.session_state['nilai_organisasi_sma']:.2f}"
                )
        

        st.divider()

        nr = st.session_state.get("nilai_rapot_sma")
        tka = st.session_state.get("nilai_tka_sma")
        sp = st.session_state.get("nilai_prestasi_sma")
        org = st.session_state.get("nilai_organisasi_sma")
        print(nr,tka,sp, org)

        st.markdown("""
            <h2 style='text-align:center;color:#D60000'>
            📊 HASIL AKHIR PERHITUNGAN
            </h2>
        """, unsafe_allow_html=True)

        st.latex(
            r"NA = (0.50 \times NRR) + (0.40 \times NRTKA) + NK + NO"
        )

        if nr is not None and tka is not None and sp is not None:

            if sp == "Langsung Diterima":

                st.success(
                    "🎉 Siswa memenuhi kategori LANGSUNG DITERIMA berdasarkan prestasi."
                )

            else:

                nilai_akhir = hitung_nilai_akhir_sma(
                    nr,
                    tka,
                    sp,
                    org
                )

                col1, col2, col3, col4, col5 = st.columns(5)

                with col1:
                    st.metric("📖 Nilai Rapor", f"{nr:.2f}")

                with col2:
                    st.metric("📝 Nilai TKA", f"{tka:.2f}")

                with col3:
                    st.metric("🏆 Skor Prestasi", f"{sp:.2f}")

                with col4:
                    st.metric("🎯 Nilai Organisasi", f"{org:.2f}")

                with col5:
                    st.metric("🎯 Nilai Akhir", f"{nilai_akhir:.2f}")