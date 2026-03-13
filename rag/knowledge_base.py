DOCUMENTS = [

    # ===== EDA INSIGHTS =====
    {
        "id": "eda_degradation",
        "text": """
        Exploratory Data Analysis shows that aircraft engine degradation is gradual and progressive.
        Sensor values evolve smoothly over cycles rather than changing abruptly.
        This confirms that engine health depends on historical behavior, not single-cycle snapshots.
        """
    },

    {
        "id": "eda_engine_variability",
        "text": """
        Different engines fail at different cycle lengths.
        Absolute sensor values differ across engines, meaning fixed thresholds are ineffective.
        Models must learn degradation patterns instead of static limits.
        """
    },

    {
        "id": "eda_sensor_behavior",
        "text": """
        Some sensors remain nearly constant throughout engine life and provide little information.
        Other sensors show increasing variance and monotonic trends near failure.
        These sensors dominate degradation behavior in late life.
        """
    },

    # ===== LSTM DESIGN DECISIONS =====
    {
        "id": "lstm_sequence_logic",
        "text": """
        The LSTM model is trained on sliding windows of sensor data.
        Each input sample consists of a fixed-length sequence of consecutive cycles.
        This allows the model to learn cumulative degradation rather than isolated readings.
        """
    },

    {
        "id": "lstm_rul_definition",
        "text": """
        Remaining Useful Life (RUL) is computed as the difference between the final cycle of an engine
        and the current cycle. RUL is capped to prevent large early-life values from dominating training.
        """
    },

    {
        "id": "lstm_why_chosen",
        "text": """
        LSTM is chosen because it explicitly models temporal dependencies.
        Engine degradation is a time-dependent process where past behavior influences current health.
        LSTM memory approximates the hidden health state of the engine.
        """
    },

    # ===== DATASET SCOPE =====
    {
        "id": "dataset_scope",
        "text": """
        FD0001 contains a single operating condition and single fault mode, making it suitable
        for building and validating a complete prognostics system.
        FD0002 introduces multiple operating conditions, increasing complexity.
        """
    }
]
