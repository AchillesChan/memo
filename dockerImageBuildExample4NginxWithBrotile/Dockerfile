# ---------- Build stage ----------
FROM alpine:3.19 AS builder

ARG NGINX_VERSION=1.28.0
ARG NGX_BROTLI_REPO=https://github.com/google/ngx_brotli.git
ARG NGINX_URL=http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz

RUN apk add --no-cache \
      build-base \
      pcre-dev \
      zlib-dev \
      openssl-dev \
      brotli-dev \
      linux-headers \
      ca-certificates \
      git \
      curl

WORKDIR /build
RUN wget ${NGINX_URL} \
 && tar xzf nginx-${NGINX_VERSION}.tar.gz

RUN git clone --depth 1 ${NGX_BROTLI_REPO} ngx_brotli \
 && cd ngx_brotli \
 && git submodule update --init --recursive || true

WORKDIR /build/nginx-${NGINX_VERSION}

RUN ./configure \
      --prefix=/etc/nginx \
      --sbin-path=/usr/sbin/nginx \
      --conf-path=/etc/nginx/nginx.conf \
      --pid-path=/var/run/nginx.pid \
      --modules-path=/usr/lib/nginx/modules \
      --error-log-path=/var/log/nginx/error.log \
      --http-log-path=/var/log/nginx/access.log \
      --with-compat \
      --with-http_ssl_module \
      --with-http_v2_module \
      --with-pcre \
      --with-file-aio \
      --with-threads \
      --with-cc-opt="-I/usr/include" \
      --with-ld-opt="-L/usr/lib" \
      --add-dynamic-module=/build/ngx_brotli \
 && make -j"$(nproc)" \
 && make install

# ---------- Runtime stage ----------
FROM alpine:3.19

ARG NGINX_VERSION=1.28.0

RUN apk add --no-cache \
      pcre \
      zlib \
      openssl \
      brotli \
      ca-certificates \
      curl \
      tzdata

# Create nginx user & group
RUN addgroup -S nginx \
 && adduser -S -G nginx -h /var/lib/nginx -s /sbin/nologin nginx

# Copy runtime files from builder
COPY --from=builder /usr/sbin/nginx /usr/sbin/nginx
COPY --from=builder /usr/lib/nginx /usr/lib/nginx
COPY --from=builder /etc/nginx /etc/nginx

# Prepare runtime directories and give ownership to nginx user
RUN mkdir -p /var/log/nginx /var/cache/nginx/client_body_temp \
             /var/cache/nginx/proxy_temp /var/cache/nginx/fastcgi_temp \
             /var/cache/nginx/scgi_temp /var/cache/nginx/uwsgi_temp \
             /var/run /usr/share/nginx/html \
 && chown -R nginx:nginx /var/log/nginx /var/cache/nginx /var/run /usr/share/nginx /var/lib/nginx

RUN mkdir -p /var/run /var/log/nginx /var/cache/nginx \
 && chown -R nginx:nginx /var/run /var/log/nginx /var/cache/nginx 


# Minimal index page
RUN printf '%s\n' '<!doctype html><html><head><meta charset="utf-8"><title>nginx 1.28</title></head><body><h1>nginx 1.28 + brotli</h1></body></html>' \
    > /usr/share/nginx/html/index.html \
 && chown nginx:nginx /usr/share/nginx/html/index.html

# Replace nginx.conf: remove "user" and "daemon", set temp paths to /var/cache/nginx
RUN rm -f /etc/nginx/nginx.conf
WORKDIR ./
ADD ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

HEALTHCHECK --interval=5s --timeout=2s --start-period=6s --retries=5 \
  CMD curl -fsS http://127.0.0.1:8080/ || exit 1

# run as non-root unix user 'nginx' (master process will run as that user)
USER nginx

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
