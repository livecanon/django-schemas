FROM python:3.11-buster as build
WORKDIR /usr/src/app
COPY ../../ .
RUN pip install pip -U
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput

FROM nginx:stable
COPY --from=build /usr/src/app/staticfiles /usr/share/nginx/html
COPY --from=build /usr/src/app/nginx.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf

# Serving django files from a separate image
