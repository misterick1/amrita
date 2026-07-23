import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

// Базовый URL твоего каталога на PartnerPage
const PARTNERPAGE_BASE_URL = 'https://partnerpage.io'

export function middleware(request: NextRequest) {
  const { pathname, search } = request.nextUrl

  // Перехватываем запросы, которые идут на страницу партнеров
  if (!pathname.startsWith('/partners')) {
    return NextResponse.next()
  }

  // Вычисляем относительный путь для отправки на PartnerPage
  const relativePath = pathname.replace('/partners', '')
  const upstreamUrl = `${PARTNERPAGE_BASE_URL}${relativePath}${search}`

  // Извлекаем IP-адрес пользователя для проброса в заголовки
  const clientIP = request.headers.get('x-forwarded-for') || request.ip || ''
  
  // Клонируем текущие заголовки и добавляем обязательные параметры от PartnerPage
  const requestHeaders = new Headers(request.headers)
  
  requestHeaders.set('X-Forwarded-For', clientIP)
  requestHeaders.set('X-Real-IP', clientIP)
  requestHeaders.set('PartnerPage-Client-IP', clientIP)
  requestHeaders.set('PartnerPage-Reverse-Proxy', 'true')
  requestHeaders.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate')

  // Перенаправляем трафик «на лету» без изменения URL в браузере клиента
  return NextResponse.rewrite(new URL(upstreamUrl, request.url), {
    request: { headers: requestHeaders },
  })
}

// Конфигурация триггера: применяется к /partners и всем вложенным путям
export const config = {
  matcher: ['/partners/:path*'],
}
