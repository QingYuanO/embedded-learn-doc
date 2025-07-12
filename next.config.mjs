import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
  output: 'export',
  images: {
    unoptimized: true,
    remotePatterns: [{ protocol: 'https', hostname: process.env.NEXT_PUBLIC_IMAGE_HOST }],
  },
};

export default withMDX(config);
