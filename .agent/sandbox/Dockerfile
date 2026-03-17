FROM kalilinux/kali-rolling

# Update and install foundational tools required by agents
# Using DEBIAN_FRONTEND=noninteractive to prevent prompts during build
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    nmap \
    radare2 \
    python3 \
    python3-pip \
    python3-venv \
    gdb \
    curl \
    checksec \
    file \
    binutils \
    strace \
    ltrace \
    iproute2 \
    openvpn \
    && rm -rf /var/lib/apt/lists/*

# Add a non-root user for executing non-privileged commands, if necessary.
# However, CTF agents often need root for tools like nmap OS detection or openvpn.
# We'll stick to root by default, but rely on Docker isolation (--cap-drop, --network=none).

# Set the primary working directory.
# This matches where the host volume will be mounted (-v $PWD:/workspace)
WORKDIR /workspace

# A simple sleep loop keeps the container running indefinitely
# so the agent can execute commands dynamically via `docker exec`.
CMD ["sleep", "infinity"]
